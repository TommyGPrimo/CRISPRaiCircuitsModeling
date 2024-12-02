# CRISPRaiCircuitsModeling
Package for modeling CRISPRa genetic circuit behavior in the prescence of competing gRNAs for multi-gene programming

# Overview
Gene regulatory networks (GRNs) comprise complex interactions that are hard to predict in CRISPRa genetic circuits due to gRNA competition for CRISPRa machinery. This issue reduces predictability of designing large genetic circuit for multi-gene metabolic programming

## Scope

*Version 1.0*
- Build CRISPRa biochemical genetic circuit implementation for modality Two: gRNA guided CRISPRa and interactions for changing parameters
- Deliverable: Bioengineering 537 Computational biology, End of Autumn 2024.
    - Working, downloadable model for checking resources, changing resources, and plotting I/O responses

*Version 1.1*
- Integrate experimental kinetic data for modality two interactions for potential autoregulator work

# Folders
## Docs
- Functional Specification: Document contains background of package, problem being addressed, user profile and use cases
- Component Specification: Document contains software components, high level description of data and provisions, interactions to accomplish the use cases and preliminary plan
- Biochemical Equations: Document contains the biochemical equations used to structure the CRISPRai genetic circuits.

## srcs
The source folder contains the main code for running this package, including unit tests and helper python scripts

## Getting Started
1. Install package using `pip install crisprai_model`
2. Initialize a CRISPRa object module.
    1. This constructs the Tellurium model for managing all CRISPRa components from d
    2. Plot mechanistic reaction
3. Define number of competing gRNAs and define type as either scRNA or sgRNA, allow plotting
    1. Default at 0 guides
    2. Plots mechanistic reaction
4. 
