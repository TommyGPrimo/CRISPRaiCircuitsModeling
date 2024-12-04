# Component Specification
The component specification for displaying and managing data, inputs required and outputs provided, as well as interactions to accomplish use cases.
## Software components

### Class
- `crisprai_model.py`: the main class used for constructing the biochemical models and outputing/plotting results
    - Generates the CRISPRai genetic model for specifying genetic targets and components

### Functions

1. `cai.get_crispra_model`
    - returns the CRISPRa model string to use in tellurium
    - Output:
        - model string of biochemical interactions

2. `cai.change_concentration_of_machinery()`
    - Allows researcher to change the different components of the crispra model and understand behavior
    - Output:
        - the tellurium model
3. `cai.simulate_crispra_model()`
    - Simulates the CRISPRa biochemical model
4. `cai.plot_crispra_model()`
    - Plots the biochemical model
5. `cai.get_io_model()`
    - Returns the io biochemical reaction based on CRISPRa model
    - Output:
        - biochemical reaction string
6. `cai.plot_io_model()`
    - Plots the I/O response from the biochemical model
7. `cai.change_steady_state_values()`
    - The main function that runs through the steady state functions and resimulates depending on inducer range used
8. `cai.visualize_io_response()`
    - Visualize a comparison of complex changes response as you change inducers. This can be used to compare the different concentrations of protein complexes and when they would reach stead-state first. i.e. lower inducer may be needed to reach high protein concentration saturation.
    - NOTE: Iterate on this so that you include cellular growth and behavior to see what it can tolerate, likely expression will go down at some point
