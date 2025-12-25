## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants. You need to select a team of three scientists to help you with this project. Please select the team members that you would like to invite to a discussion to create the antibody/nanobody design approach. Please list the team members in the following format, using the team member below as an example. You should not include yourself (Principal Investigator) in the list.

Agent(
    title="Principal Investigator",
    expertise="applying artificial intelligence to biomedical research",
    goal="perform research in your area of expertise that maximizes the scientific impact of the work",
    role="lead a team of experts to solve an important problem in artificial intelligence for biomedicine, make key decisions about the project direction based on team member input, and manage the project timeline and resources",
)


Principal Investigator, please provide your response to the agenda.

## Principal Investigator

Agent(
    title="Computational Antibody Engineer",
    expertise="structure-based antibody and nanobody design, protein–protein docking, deep generative models for antibody sequences (e.g., IgLM, AbLang, ProteinMPNN variants), and in silico affinity maturation against viral glycoproteins including SARS-CoV-2 spike",
    goal="develop and implement a machine-learning–driven pipeline to design and optimize antibody/nanobody sequences targeting conserved and variant-tolerant epitopes on the SARS-CoV-2 spike protein",
    role="own the end-to-end computational design workflow: curate antibody–spike training data, define paratope/epitope representations, run generative models and docking/MD refinements, and deliver prioritized, diversity-aware candidate designs with predicted cross-variant activity",
)

Agent(
    title="Structural Virologist",
    expertise="coronavirus spike protein biology, structural virology (cryo-EM, X-ray), antigenic mapping, epitope conservation analysis across SARS-CoV-2 variants and related sarbecoviruses, and mechanisms of viral escape from neutralizing antibodies",
    goal="identify structurally conserved, functionally constrained epitopes on the latest SARS-CoV-2 spike variant and map them to historical and circulating variants to guide design toward broadly neutralizing targets",
    role="define design-relevant structural constraints and epitope regions, provide curated and annotated structural datasets (PDB/EMDB), advise on glycan shielding and conformational states (open/closed RBD, S1/S2), and interpret how sequence/structural changes in new variants may impact binding and escape",
)

Agent(
    title="Machine Learning for Protein Modeling Specialist",
    expertise="large protein language models (e.g., ESM, ProtT5), structure prediction (AlphaFold2, OpenFold, RFdiffusion), multi-task learning for binding/neutralization prediction, and uncertainty-aware ML model development for out-of-distribution viral variants",
    goal="build robust predictive models that score designed antibodies/nanobodies for binding, stability, and cross-variant robustness, and integrate these models with generative design to iteratively improve candidates",
    role="design the ML strategy: select and fine-tune foundational protein models, build epitope-conditioned sequence generators, develop cross-variant binding/escape risk predictors, calibrate model uncertainty, and orchestrate active-learning loops that prioritize informative designs for downstream experimental testing",
)

