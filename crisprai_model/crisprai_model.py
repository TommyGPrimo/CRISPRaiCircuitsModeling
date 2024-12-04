
# Tommy G. Primo, Fall 2024

# Import functions
import tellurium as te
import numpy as np
import matplotlib.pyplot as plt

class crisprai_model:
    
    def get_crispra_model(self):
        """
        Returns the crispra model function and plots the model
        """
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
    
    def change_concentration_of_machinery(self,model,dcas_9=2,guide=2,complex=0,target=6):
        model.reset()
        model.d=dcas_9
        model.s = guide
        model.A = complex
        model.D = target
        self.simulate_crispra_model(model=model)

    def simulate_crispra_model(self, model, time=10):
        m = te.loada(model)
        mm = m.simulate(0,time,2000)
        return [m,mm]
    
    def plot_crispra_model(self,model):
        model.plot(title="CRISPRa tethered Model", xlabel= "Time (sec)", ylabel= "Concentration")
    
    def get_io_model(self):
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
        return reduced_model
    
    # Simulate the IO model
    def simulate_io_model(self, reduced_model):
        rm = te.loada(reduced_model)
        rm_data = rm.simulate(0,1,2000)
        return [rm,rm_data]
    
    def plot_io_model(self,io):
        io.plot(title="CRISPRa IO Model", xlabel= "Time (sec)", ylabel= "Concentration")
    
    # Define function to change steady state values with changing inducer for io plotting
    def change_steady_state_values(self,tellurium_model, inducer_concentrations, steady_state_protein_list):
        for inducer in inducer_concentrations:
            tellurium_model.u1 = inducer
            simulated_model = tellurium_model.simulate()
            simulated_steady_state_proteins = simulated_model['[Y]'][-1]
            steady_state_protein_list.append(simulated_steady_state_proteins)
    
    def visualize_io_response(self, rm_model, inducer_range, complex_comparisons):
        # rest the reduced model
        rm_model.reset()
        
        # Define varying inducer values
        inducer_values = np.logspace(-inducer_range,inducer_range, 100)
        
        # Define empty steadyStateProteinsList for two conditions
        steady_state_condition_1 = []
        steady_state_condition_2 = []
        
        # Change complex concentration and populate steady state concentrations
        rm_model.d = complex_comparisons[0]
        self.change_steady_state_values(rm_model, inducer_values, steady_state_condition_1)
        
        # Rest model
        rm_model.reset()
        
        # Change complex concentrations and populate steady state concentrations for secondary comparison
        rm_model.d = complex_comparisons[1]
        self.change_steady_state_values(rm_model, inducer_values, steady_state_condition_2)
        
        # Nested function for plotting io response
        def plot_io(input, ss_protein_concentrations,color = 'black'):
            plt.plot(input, ss_protein_concentrations, color)
        
        # Plotting the io responses
        plot_io(inducer_values, steady_state_condition_1)
        plot_io(inducer_values, steady_state_condition_2, 'red')
        
        # Setting up the plot descriptions and information
        plt.xlabel('$inducer_i$ ')
        plt.ylabel('$Protein_i$')
        plt.xscale('log')
        plt.title('CRISPRa I/O Response')

        red_patch = plt.Line2D([0], [0], color='red', lw=2, label=f'complex={complex_comparisons[1]}')
        grey_patch = plt.Line2D([0], [0], color='black', lw=2, label=f'complex={complex_comparisons[0]}')
        plt.legend(handles=[red_patch, grey_patch], loc='lower right', fontsize=11); # Semi-colon to remove print statement 
        plt.show()
        
        