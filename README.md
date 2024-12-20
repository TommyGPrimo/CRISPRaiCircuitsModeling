# CRISPRaiCircuitsModeling
Package for modeling CRISPRa behavior and mainly seeing the I/O response to comparisons between CRISPRa-complexes

## Scope

*Version 1.0*
- Build CRISPRa biochemical genetic circuit implementation of tethered complexes: gRNA guided CRISPRa and interactions for changing parameters
- Deliverable: Bioengineering 537 Computational biology, End of Autumn 2024.
    - Working, downloadable model for checking resources, changing resources, and plotting I/O responses

*Version 1.1*
- changing kinetics
- implementation of RNA-guided CRISPRa complexes

# Folders
## Docs
- Functional Specification: Document contains background of package, problem being addressed, user profile and use cases
- Component Specification: Document contains software components, high level description of data and provisions, interactions to accomplish the use cases and preliminary plan

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
