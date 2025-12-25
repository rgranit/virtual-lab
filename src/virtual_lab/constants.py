"""Holds constants."""

DEFAULT_MODEL = "gpt-4o-2024-08-06"

MODEL_TO_INPUT_PRICE_PER_TOKEN = {
    # Prices in $ per token (i.e., $ per 1M tokens ÷ 1e6)
    "gpt-3.5-turbo-0125": 0.50 / 10**6,         # $0.50 per 1M input
    "gpt-4o-2024-08-06": 2.50 / 10**6,          # $2.50 per 1M input
    "gpt-4o-2024-05-13": 5.00 / 10**6,          # $5.00 per 1M input
    "gpt-4o-mini-2024-07-18": 0.15 / 10**6,     # $0.15 per 1M input
    "o1-mini-2024-09-12": 1.10 / 10**6,         # $1.10 per 1M input

    # GPT-4.1 series
    "gpt-4.1": 2.00 / 10**6,                    # $2.00 per 1M input (GPT-4.1 base) :contentReference[oaicite:1]{index=1}

    # GPT-5 series
    "gpt-5.1": 1.25 / 10**6,                    # ~$1.25 per 1M input (flagship) :contentReference[oaicite:2]{index=2}
    "gpt-5.2": 1.75 / 10**6,                    # ~$1.75 per 1M input (latest) :contentReference[oaicite:3]{index=3}
}

MODEL_TO_OUTPUT_PRICE_PER_TOKEN = {
    "gpt-3.5-turbo-0125": 1.50 / 10**6,         # $1.50 per 1M output
    "gpt-4o-2024-08-06": 10.00 / 10**6,         # $10.00 per 1M output
    "gpt-4o-2024-05-13": 15.00 / 10**6,         # $15.00 per 1M output
    "gpt-4o-mini-2024-07-18": 0.60 / 10**6,     # $0.60 per 1M output
    "o1-mini-2024-09-12": 4.40 / 10**6,         # $4.40 per 1M output

    # GPT-4.1 series
    "gpt-4.1": 8.00 / 10**6,                    # $8.00 per 1M output (GPT-4.1 base) :contentReference[oaicite:4]{index=4}

    # GPT-5 series
    "gpt-5.1": 10.00 / 10**6,                   # ~$10.00 per 1M output (flagship) :contentReference[oaicite:5]{index=5}
    "gpt-5.2": 14.00 / 10**6,                   # ~$14.00 per 1M output (latest) :contentReference[oaicite:6]{index=6}
}


FINETUNING_MODEL_TO_INPUT_PRICE_PER_TOKEN = {
    "gpt-4o-2024-08-06": 3.75 / 10**6,
    "gpt-4o-mini-2024-07-18": 0.3 / 10**6,
}

FINETUNING_MODEL_TO_OUTPUT_PRICE_PER_TOKEN = {
    "gpt-4o-2024-08-06": 15 / 10**6,
    "gpt-4o-mini-2024-07-18": 1.2 / 10**6,
}

FINETUNING_MODEL_TO_TRAINING_PRICE_PER_TOKEN = {
    "gpt-4o-2024-08-06": 25 / 10**6,
    "gpt-4o-mini-2024-07-18": 3 / 10**6,
}

DEFAULT_FINETUNING_EPOCHS = 4

CONSISTENT_TEMPERATURE = 0.2
CREATIVE_TEMPERATURE = 0.8

PUBMED_TOOL_NAME = "pubmed_search"
PUBMED_TOOL_DESCRIPTION = {
    "type": "function",
    "function": {
        "name": PUBMED_TOOL_NAME,
        "description": "Get abstracts or the full text of biomedical and life sciences articles from PubMed Central.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to use to search PubMed Central for scientific articles.",
                },
                "num_articles": {
                    "type": "integer",
                    "description": "The number of articles to return from the search query.",
                },
                "abstract_only": {
                    "type": "boolean",
                    "description": "Whether to return only the abstract of the articles.",
                },
            },
            "required": ["query", "num_articles"],
        },
    },
}
