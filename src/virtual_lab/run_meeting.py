"""Runs a meeting with LLM agents."""

import json
import time
from pathlib import Path
from typing import Literal

from openai import OpenAI
from tqdm import trange, tqdm

from virtual_lab.agent import Agent
from virtual_lab.constants import CONSISTENT_TEMPERATURE, PUBMED_TOOL_DESCRIPTION, PUBMED_TOOL_NAME
from virtual_lab.prompts import (
    individual_meeting_agent_prompt,
    individual_meeting_critic_prompt,
    individual_meeting_start_prompt,
    SCIENTIFIC_CRITIC,
    team_meeting_start_prompt,
    team_meeting_team_lead_initial_prompt,
    team_meeting_team_lead_intermediate_prompt,
    team_meeting_team_lead_final_prompt,
    team_meeting_team_member_prompt,
)
from virtual_lab.utils import (
    convert_messages_to_discussion,
    count_discussion_tokens,
    count_tokens,
    get_summary,
    print_cost_and_time,
    run_pubmed_search,
    save_meeting,
)


def run_meeting(
    meeting_type: Literal["team", "individual"],
    agenda: str,
    save_dir: Path,
    save_name: str = "discussion",
    team_lead: Agent | None = None,
    team_members: tuple[Agent, ...] | None = None,
    team_member: Agent | None = None,
    agenda_questions: tuple[str, ...] = (),
    agenda_rules: tuple[str, ...] = (),
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
    num_rounds: int = 0,
    temperature: float = CONSISTENT_TEMPERATURE,
    pubmed_search: bool = False,
    return_summary: bool = False,
) -> str:
    """Runs a meeting with a LLM agents.

    :param meeting_type: The type of meeting.
    :param agenda: The agenda for the meeting.
    :param save_dir: The directory to save the discussion.
    :param save_name: The name of the discussion file that will be saved.
    :param team_lead: The team lead for a team meeting (None for individual meeting).
    :param team_members: The team members for a team meeting (None for individual meeting).
    :param team_member: The team member for an individual meeting (None for team meeting).
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :param agenda_rules: The rules for the meeting.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :param num_rounds: The number of rounds of discussion.
    :param temperature: The sampling temperature.
    :param pubmed_search: Whether to include a PubMed search tool.
    :param return_summary: Whether to return the summary of the meeting.
    :return: The summary of the meeting (i.e., the last message) if return_summary is True, else None.
    """
    # Validate meeting type
    if meeting_type == "team":
        if team_lead is None or team_members is None or len(team_members) == 0:
            raise ValueError("Team meeting requires team lead and team members")
        if team_member is not None:
            raise ValueError("Team meeting does not require individual team member")
        if team_lead in team_members:
            raise ValueError("Team lead must be separate from team members")
        if len(set(team_members)) != len(team_members):
            raise ValueError("Team members must be unique")
    elif meeting_type == "individual":
        if team_member is None:
            raise ValueError("Individual meeting requires individual team member")
        if team_lead is not None or team_members is not None:
            raise ValueError(
                "Individual meeting does not require team lead or team members"
            )
    else:
        raise ValueError(f"Invalid meeting type: {meeting_type}")

    # Start timing the meeting
    start_time = time.time()

    # Set up client
    client = OpenAI()

    # Set up team
    if meeting_type == "team":
        team = [team_lead] + list(team_members)
    else:
        team = [team_member] + [SCIENTIFIC_CRITIC]

    # Set up tools
    tools = [PUBMED_TOOL_DESCRIPTION] if pubmed_search else None

    # Map agent titles for discussion conversion
    agent_title_to_title = {agent.title: agent.title for agent in team}

    # Set up tool token count
    tool_token_count = 0

    # Set up conversation history (list of messages)
    messages = []

    # Initial prompt for team meeting
    if meeting_type == "team":
        messages.append({
            "role": "user",
            "content": team_meeting_start_prompt(
                team_lead=team_lead,
                team_members=team_members,
                agenda=agenda,
                agenda_questions=agenda_questions,
                agenda_rules=agenda_rules,
                summaries=summaries,
                contexts=contexts,
                num_rounds=num_rounds,
            ),
        })

    # Loop through rounds
    for round_index in trange(num_rounds + 1, desc="Rounds (+ Final Round)"):
        round_num = round_index + 1

        # Loop through team and elicit responses
        for agent in tqdm(team, desc="Team"):
            # Prompt based on agent and round number
            if meeting_type == "team":
                # Team meeting prompts
                if agent == team_lead:
                    if round_index == 0:
                        prompt = team_meeting_team_lead_initial_prompt(
                            team_lead=team_lead
                        )
                    elif round_index == num_rounds:
                        prompt = team_meeting_team_lead_final_prompt(
                            team_lead=team_lead,
                            agenda=agenda,
                            agenda_questions=agenda_questions,
                            agenda_rules=agenda_rules,
                        )
                    else:
                        prompt = team_meeting_team_lead_intermediate_prompt(
                            team_lead=team_lead,
                            round_num=round_num - 1,
                            num_rounds=num_rounds,
                        )
                else:
                    prompt = team_meeting_team_member_prompt(
                        team_member=agent, round_num=round_num, num_rounds=num_rounds
                    )
            else:
                # Individual meeting prompts
                if agent == SCIENTIFIC_CRITIC:
                    prompt = individual_meeting_critic_prompt(
                        critic=SCIENTIFIC_CRITIC, agent=team_member
                    )
                else:
                    if round_index == 0:
                        prompt = individual_meeting_start_prompt(
                            team_member=team_member,
                            agenda=agenda,
                            agenda_questions=agenda_questions,
                            agenda_rules=agenda_rules,
                            summaries=summaries,
                            contexts=contexts,
                        )
                    else:
                        prompt = individual_meeting_agent_prompt(
                            critic=SCIENTIFIC_CRITIC, agent=team_member
                        )

            # Create message from user to agent
            messages.append({
                "role": "user",
                "content": prompt,
            })

            # Prepare messages for this agent (include system message)
            agent_messages = [
                {"role": "system", "content": agent.prompt},
            ] + messages

            # Run the agent with function calling support
            while True:
                response = client.chat.completions.create(
                    model=agent.model,
                    messages=agent_messages,
                    temperature=temperature,
                    tools=tools,
                )

                # Add assistant response to messages
                assistant_message = response.choices[0].message

                # Check if function calling is required
                if assistant_message.tool_calls:
                    # Add assistant message with tool calls to conversation
                    assistant_message_dict = {
                        "role": "assistant",
                        "content": assistant_message.content or "",
                        "tool_calls": [
                            {
                                "id": tool_call.id,
                                "type": "function",
                                "function": {
                                    "name": tool_call.function.name,
                                    "arguments": tool_call.function.arguments,
                                },
                            }
                            for tool_call in assistant_message.tool_calls
                        ],
                        "agent_title": agent.title,  # Track which agent responded
                    }
                    agent_messages.append(assistant_message_dict)
                    
                    # Also add to main messages for discussion tracking
                    messages.append({
                        "role": "assistant",
                        "content": assistant_message.content or "",
                        "agent_title": agent.title,
                    })

                    # Run the tools
                    tool_outputs = []
                    for tool_call in assistant_message.tool_calls:
                        if tool_call.function.name == PUBMED_TOOL_NAME:
                            # Extract the query from the tool arguments
                            args_dict = json.loads(tool_call.function.arguments)
                            # Run the tool
                            output = run_pubmed_search(**args_dict)
                            tool_outputs.append({
                                "tool_call_id": tool_call.id,
                                "output": output,
                            })
                        else:
                            raise ValueError(f"Unknown tool: {tool_call.function.name}")

                    # Update tool token count
                    tool_token_count += sum(
                        count_tokens(tool_output["output"]) for tool_output in tool_outputs
                    )

                    # Add tool outputs to messages (Chat Completions API format)
                    for tool_output in tool_outputs:
                        agent_messages.append({
                            "role": "tool",
                            "tool_call_id": tool_output["tool_call_id"],
                            "content": tool_output["output"],
                        })

                    # Add tool outputs to main conversation for later rounds
                    messages.append({
                        "role": "user",
                        "content": "Tool Output:\n\n"
                        + "\n\n".join(
                            tool_output["output"] for tool_output in tool_outputs
                        ),
                    })
                else:
                    # No function calling needed, add response to main conversation
                    messages.append({
                        "role": "assistant",
                        "content": assistant_message.content or "",
                        "agent_title": agent.title,  # Track which agent responded
                    })
                    break

            # If final round, only team lead or team member responds
            if round_index == num_rounds:
                break

    # Convert messages to discussion format
    discussion = convert_messages_to_discussion(
        messages=messages, agent_title_to_title=agent_title_to_title
    )

    # Count discussion tokens
    token_counts = count_discussion_tokens(discussion=discussion)

    # Add tool token count to total token count
    token_counts["tool"] = tool_token_count

    # Print cost and time
    # TODO: handle different models for different agents
    print_cost_and_time(
        token_counts=token_counts,
        model=team_lead.model if meeting_type == "team" else team_member.model,
        elapsed_time=time.time() - start_time,
    )

    # Save the discussion as JSON and Markdown
    save_meeting(
        save_dir=save_dir,
        save_name=save_name,
        discussion=discussion,
    )

    # Optionally, return summary
    if return_summary:
        return get_summary(discussion)
