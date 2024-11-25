# Functional specification

## Background
CRISPR-based activation and interference (CRISPRai) allows bioengineers to up-regulate and down-regulate gene expression to control metabolism via gRNA targeting within gene-circuits. In order to build predictable large-scale genetic circuits researchers need to predictable modeling of gene expression by controlling concentrations of dCas9, Activator-complex, and gRNAs in the prescence of competitor gRNAs that use up protein resources

### The Tool
This biochemical tool models gRNA interactions for CRISPRa-machinery and allows researcher to modulate components and view I/O response of gene expression.
1. First the user specifies which type of CRISPRa model they want, either fused-CRISPR-activation or RNA guided CRISPR-activation to construct the appropriate CRISPRa model for continuation, plots time-components and prints concentration of machinery parameters
2. Second the user modifies concentrations to view changes and comparison-plots for gene expression response

## User profile
The target users are researchers and bioengineers who are involved in building genetic circuits, specifically CRISPR-based genetic circuits with an emphasis on CRISPRai.
The users include undergraduates, graduates, research technicians, post-docs, principal investigators, scientists, and even hobbyists without lab access

### Skills and Access
- User should have a beginner to intermediate python programming skills
- User should have a basic understanding of python package installation such as `pip install` or Jupyter Notebook
- User should have a basic understanding of basic [CRISPR-based activation and interference technology](https://www.synthego.com/guide/crispr-methods/crispri-crispra)
- User should have a basic understanding of [Principles of genetic circuits](https://www.nature.com/articles/nmeth.2926)

### Usecases
Objective: The user intends to understand the effect of gene expression of their target gene in the prescence of competitor gRNAs that use up the CRISPRa-resources.
1. Install package and initialize CRISPRa biochemical model
2. Decide number of competitor guides
3. Plot I/O response
4. Change CRISPRa-machinery concentrations, *When changing machinery inputing array allows you to compare I/O response of different concentrations*
5. Plot I/O response again

### Expectation
1. The user should expect an I/O plot describing the expression of target gene based on changing the concentrations of their CRISPRa-machinery to influence experimental design
2. The user should expect the I/O plot to change depending when changing different parameters to understand underlying circuit changes.

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