
# Tommy G. Primo, Fall 2024

# Import functions
import tellurium as te
import numpy as np
import matplotlib.pyplot as plt

class crisprai_model:
    
    def create_model():
        # Define CRISPRa modality two model - scRNA recruited activator protein complex coupled with dCas9
        model = """
        # CRISPRa Modality 1 - dCas9 tethered to activator model

        # Specify chemical reactions

        R1: d + s -> A; ki_1*d*s-ki_2*A
        R2: A + D -> c; li_1*A*D-li_2*c
        R3: c -> Y; kappa*c

        R4: Y -> ; gam*Y;
        R5: s -> ; del*s;


        # Initial concentrations values
        d = 2
        s = 2
        A = 2
        D = 6

        # Kinetic parameters
        ki_1 = 5;
        ki_2 = 0.1;
        li_1 = 4;
        li_2 = 1;
        kappa = 1;
        gam = 1;
        del = 1;
        """
        return model
        
    def change_machinery(crispr_complex=1, target_gene=1):
        
        """ChangeCRISPRMachineryConcentration - This function allows user to change the concentration of the CRISPRa machinery or target gene

        Args:
            crispr_complex (int, optional): dCas9-Activator tethered complex concentration. Defaults to 1.
            target_gene (int, optional): the target gene for your desired gene activation. Defaults to 1.
        """
        print("Machinery Changed")

    def simulate_crispra_model(model, time=10):
        """ simulateGeneticCircuits
        - Generates a tellurium simulation of the steady state response of the input
        Args:
            model (tellurium): The tellurium model needed to simulate the plot
            time (int): The time to measure concentrations
        """
        rr = te.loada(model)
        model_data = rr.simulate(0,time,200)
        rr.plot(title="CRISPRa Modality I Model", xlabel= "Time (sec)", ylabel= "Concentration")
        return model_data

    def define_io_model():
        
        # Reduced ODE model
        reduced_model = """
        # Reactions
        R0: -> s1; u1-del*s1;
        R1: -> Y; ((kap*D*d*s1)/(d*s1 + K_k*K_l)) - gam*Y

        # Competing reactions
        R2: -> s2; u2-del*s2;
        R3: -> Y2; ((kap*D2*d*s2)/(d*s2 + K_k*K_l)) - gam*Y2

        # Parameters
        u1 = 1;
        u2 = 2000;

        del = 1;
        gam = 1;

        kap = 1000;
        D = 10;
        D2 = 10;
        K_k = 5;
        K_l = 3;
        d = 100;
        """
        
            # Initialize reduced tellurium model
        rtm = te.loada(reduced_model)
        rm_data = rm.simulate(0,1,2000)
        
        # If plotting is needed - uncomment
        #rtm.plot(title="CRISPRa Modality I Model", xlabel= "Time (sec)", ylabel= "Concentration")
        return rtm

    def simulate_io_response(rm):
        # Reset the tellurium model
        rm.reset()
        
        print("Simulate IO")

    # Define function to change steady
    def change_steadystate_values(tellurium_model, inducer_concentrations, steady_state_protein_list):
        for inducer in inducer_concentrations:
            tellurium_model.u1 = inducer
            simulated_model = tellurium_model.simulate()
            simulated_steady_state_protein = simulated_model['[Y]'][-1]
            steady_state_protein_list.append(simulated_steady_state_protein)
            
    def plot_io_function(input, steady_state_protein_concentrations,color = 'black'):
        plt.plot(input, steady_state_protein_concentrations, color)

    def define_io_plot(label):
        """define_io_plot - Function sets up plotting function for the io model
        
            Args:
                label (Array,String): Array of string comparing labels
        """
        # Plot input to output
        plt.xlabel('$inducer_i$ ')
        plt.ylabel('$Protein_i$')
        plt.xscale('log')
        plt.title('CRISPRa I/O Response')

        red_patch = plt.Line2D([0], [0], color='red', lw=2, label=label[0])
        grey_patch = plt.Line2D([0], [0], color='black', lw=2, label=label[1])
        
        plt.legend(handles=[red_patch, grey_patch], loc='lower right', fontsize=11); # Semi-colon to remove print statement 
        plt.show()
