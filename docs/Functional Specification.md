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
Objective: The user intends to understand the effect of gene expression with changing CRISPRa components and at what concentration to use and inducer to reach saturation of a protein

*Follow Tutorial in Jupyter notebook for example*

# Getting Started
1. Install package using `pip install -i https://test.pypi.org/simple/ CRISPRaiCircuitsModeling`
2. Create package `import crisprai_model as cai`
3. Define crisprai genetic circuit `cai_circuit = cai()` and get the model `cai_model = cai_circuit.get_crisprai_model()`
4. define the model simulation `cai_simulation = cai_circuit.simulate_crispra_model(cai_model, time=8)` where `8` can be any time needed
5. Plot simulation `cai_circuit.plot_crispra_model(cai_simulation[0])`
6. Change machinery concentrations `updated_model = cai_circuit.change_concentration_of_machinery(cai_simulation[0], dcas_9=2, guide=1, target=1)`
7. Plot new simulation `cai_circuit.plot_crispra_model(updated_model)`
8. Define the I/O response model `io_model = cai_circuit.get_io_model()`
9. Define the I/O simulation `io_simulation = cai_circuit.simulate_io_model(io_model)`
10. Plot the I/O response: `cai_circuit.visualize_io_response(io_simulation[0], 8, [10,1000]) `
    1. Change the last argument to see differences in complex concentration differences `[10,1000]` means 100x difference in concentration

### Expectation
1. The user should expect an I/O plot describing the expression of target gene based on changing the concentrations of their CRISPRa-machinery to influence experimental design
2. The user should expect the I/O plot to change depending when changing different parameters to understand underlying circuit changes.

## Changing Inducer ranges
*Different inducers may express at different ranges, here you can change the inducer range and replot*
1. Change the inducer range using `cai.changeInputResponseRange(responseRange)` where the `responseRange` is an array of two elements, a lower and upper bound, i.e. `[10E-8,10E8]`
2. Check changed parameters `cai.checkGeneticCircuitComponents()`
3. Simulate the biochemical model `cai.visualize_io_response()` for an I/O plot of steady state levels

## Note
*Each simulation resets through tellurium*