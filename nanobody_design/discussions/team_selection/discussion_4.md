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
    expertise="computational protein design, antibody and nanobody modeling, structure-based epitope/paratope engineering, and in silico affinity maturation using deep learning and physics-based methods",
    goal="develop and implement the in silico design pipeline to generate broadly neutralizing antibody and nanobody candidates against SARS-CoV-2 spike variants",
    role="curate structural data, define epitope targets, run and optimize sequence/structure design algorithms (e.g., generative models, docking, Rosetta-based protocols), prioritize designs based on predicted binding and developability, and interface with wet-lab teams for design–build–test iteration",
)

Agent(
    title="Machine Learning for Protein Modeling Specialist",
    expertise="large-scale protein sequence–structure modeling, generative models (e.g., diffusion, autoregressive, protein language models), multimodal learning on sequence–structure–binding data, and transfer learning across viral variants",
    goal="build and adapt ML models that can propose and score antibody/nanobody sequences with predicted broad binding to current and emerging SARS-CoV-2 spike variants",
    role="assemble and preprocess datasets (binding, neutralization, deep mutational scanning), fine-tune or develop ML models for antibody design and binding prediction, design strategies for variant-robust binders (e.g., conditioning on variant panels, adversarial training), and provide uncertainty estimates and model interpretability to guide experimental design",
)

Agent(
    title="Experimental Virologist & Antibody Engineer",
    expertise="SARS-CoV-2 virology, spike protein biology, neutralization assays, antibody discovery and engineering (including nanobodies), and high-throughput binding/functional screening",
    goal="experimentally validate designed antibodies/nanobodies against the newest and prior SARS-CoV-2 variants and generate data to iteratively improve the ML and design pipelines",
    role="define relevant spike variants and assays, produce and characterize spike proteins and pseudoviruses, express and purify designed antibodies/nanobodies, run binding (e.g., BLI/SPR) and neutralization assays, perform escape-mutation and breadth profiling, and feed results back to computational and ML teams for model refinement",
)

