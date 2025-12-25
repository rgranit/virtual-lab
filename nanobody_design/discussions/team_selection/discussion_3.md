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
    expertise="structure-based antibody and nanobody design, protein–protein interaction modeling, and deep generative models for antibody sequence optimization",
    goal="develop and implement the in silico design and optimization pipeline for broadly neutralizing antibodies/nanobodies targeting conserved regions of SARS-CoV-2 spike, including the newest and prior variants",
    role="lead structural modeling (AlphaFold/RoseTTAFold, docking), epitope/paratope mapping, generative sequence design (e.g., protein language models, diffusion models), and in silico developability/affinity screening",
)

Agent(
    title="Viral Immunologist",
    expertise="coronavirus immunology, B-cell epitope mapping, escape mutation pathways, and mechanisms of broadly neutralizing antibody responses",
    goal="define biologically plausible and conserved epitopes on spike, anticipate escape routes, and ensure designed antibodies/nanobodies target functionally constrained regions across variants",
    role="curate and interpret virological/immunological data, define design constraints and target epitopes, map variant landscapes, and guide selection of fitness-constrained regions for broad neutralization",
)

Agent(
    title="Machine Learning for Protein Design Specialist",
    expertise="large-scale protein representation learning, multimodal ML on sequence–structure–phenotype data, and active learning/optimization for protein engineering",
    goal="build and train ML models that predict binding and breadth, integrate multi-variant data, and drive iterative design cycles for improved antibodies/nanobodies",
    role="develop ML architectures (e.g., protein language models, graph neural networks, sequence-to-function predictors), design active learning strategies with in silico/experimental feedback, and implement multi-objective optimization for affinity, breadth, and developability",
)

