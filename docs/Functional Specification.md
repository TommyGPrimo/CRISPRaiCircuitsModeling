# Functional specification

## Background
CRISPR-based activation and interference (CRISPRai) allows bioengineers to regulate metabolism by up-regulating and down-regulating gene expression based on guide-RNA (gRNA) targeting.
In order to build large-scale genetic circuits for biological design towards desired phenotypical responses:

1. understanding and modeling the effects of multiple gRNA interactions is important for predictability
2. Having a tool for plotting I/O responses, allows for easier experimental design
3. understanding the modulation effects of CRISPRai-machinery allows for selecting the proper promoters for controlling their expression

### Tool
The tool runs a biochemical model of gRNA interactions with CRISPRai machinery, and plots the response of experimental inputs towards their target gene output.

## User profile
The target users are researchers and bioengineers who are involved in building genetic circuits, specifically CRISPR-based genetic circuits with an emphasis on CRISPRai.
The users include undergraduates, graduates, research technicians, post-docs, principal investigators, scientists, and even hobbyists without lab access

### Skills and Access
- User should have a basic understanding of python
- User should have a basic understanding of python pckage installation such as `pip install`
- User should have a basic understanding of basic [CRISPR-based activation and interference technology](https://www.synthego.com/guide/crispr-methods/crispri-crispra)
- User should have a basic understanding of [Principles of genetic circuits](https://www.nature.com/articles/nmeth.2926)

### Usecases
1. The user intends to understand the expression of their target gene based on the number of gRNA competitors in the system
2. The user intends to understand the expression of their target gene based on regulating the expression of CRISPRai machinery, primarily dCas9 and Activator-protein

### Expectation
1. The user should expect an I/O plot describing the expression of target gene based on changing the expression of their CRISPRai machinery
2. The user should expect the I/O plot to change depending when changing different parameters to understand underlying circuit changes.

# Getting Started - TODO: Finish this section and answer Joseph on issues
*The package is best used in through a Jupyter notebook*
1. Install the CRISPRai genetic circuits python package by `pip install crisrai_model`
2. Import the package using `import crisprai_model as cai`
3. Run the model object `cai.checkGeneticCircuitComponents()` to see the default CRISPRai genetic circuit components and parameter values
4. Run the default model using `cai.simulateGeneticCircuit()`

## Design Genetic circuit to model
Desiging the genetic circuit to model involves a 3 step process
1. Changing the CRISPRai machinery resources using `cai.changeMachineryConcentration(dCas9=1, Activator=1)` to any numerical value
2. Setting your competitor genetic circuit number which consumes your machinery resources `cai.setCompetitorCircuits(value=1)`
3. Simulating the biochemical model for the genetic circuit: `cai.simulateGeneticCircuit()` for an I/O plot of steady state levels

## Changing Inducer ranges
*Different inducers may express at different ranges, here you can change the inducer range and replot*
1. Change the inducer range using `cai.changeInputResponseRange(responseRange)` where the `responseRange` is an array of two elements, a lower and upper bound, i.e. `[10E-8,10E8]`
2. Check changed parameters `cai.checkGeneticCircuitComponents()`
3. Simulate the biochemical model `cai.simulateGeneticCircuit()` for an I/O plot of steady state levels

## Note
*Each simulation resets through tellurium*