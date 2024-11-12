# Component Specification
This section contains software component specification for displaying data, managing data, inputs required and outputs provided, as well as interactions to accomplish use cases.
## Software components

### Class
- `crisprai_model.py`: the main class used for constructing the biochemical models and outputing/plotting results
    - Generates the CRISPRai genetic model for specifying genetic targets and competitors

### Functions

1. `cai.changeMachineryConcentration(dCas9=1, Activator=1)`
    - Changes the concentration of the CRISPRai machinery
    - Arguments:
        - dCas9 Concentration: the concentration of the dCas9 protein. default is 1
        - Activator concentration: the concentration of the MCP-SoxS protein complex. default is 1
    - Output:
        - None
    - **Note**:
        - *Setting Activator to 0 would change the entire circuitry into a CRISPRi-only genetic circuit biochemical model*
2. `cai.checkGeneticCircuitComponents()`
    - Displays the parameter values for all the genetic circuit components.
        - CRISPRai machinery
        - target genetic circuit: the number of circuits
        - competitor circuits: the of competitor gRNAs
3. `cai.simulateGeneticCircuit()`
    - Simulates I/O biochemical circuit for the genetic circuit, The input being inducer or expression change experimentalist needs to do, the output being the response
    - Arguments:
        - None
    - Output:
        - Steady state tellurium plot of biochemical circuit
4. `cai.setCompetitorCircuits(value=1)`
    - Defines the number of competitor circuits.
    - Arguments:
        - value: the number of gRNAs using up CRISPRai machinery resources
    - Output:
        - None
5. `cai.setTargetGene(value=1)`
    - set the numbere of target genes to be used for reporter response
    - Arguments:
        - value: the number of gene targets
    - Output:
        - None
6. `cai.changeInputResponseRange(responseRange)`
    - Change input response range function to vary the concentration of the inducer range by inputing an array
    - Arguments:
        - A two element array defining the lower bound and upper bound of the inducer concentration
    - Output:
        - None
7. `extractSteadyStateValues()`
    - Helper function that is called when generating the I/O tellurium plots.
    - Arguments:
        - None
    - Output:
        - Steady state values for response output with changing input


## Interactions

- Location of GOI: Future update

## Preliminary Plan
1. Import the package as `import crisprai_model as cai`
2. Define the type of genetic circuit using `cai` object, such as `my_CRISPRi_circuit = cai.defineCRISPRiCircuit()`
