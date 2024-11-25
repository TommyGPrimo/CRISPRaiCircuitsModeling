
# Tommy G. Primo, Fall 2024

# Import functions
import tellurium as te
import numpy as np
import matplotlib.pyplot as plt



class crisprai_model:

    global CRISPRai_modality_one
    
    def __init__(self):
        # Define CRISPRa modality two model - scRNA recruited activator protein complex coupled with dCas9
        
        print("Module built")
        
    def defineModalityTwoGeneticCircuit():
        pass

    def simulateGeneticCircuits():
        """ simulateGeneticCircuits
        - Generates a tellurium simulation of the steady state response of the input
        """
        rr = te.loada(CRISPRai_modality_one)
        model_data = rr.simulate(0,10,200)
        rr.plot(title="CRISPRa Modality I Model", xlabel= "Time (sec)", ylabel= "Concentration")
        model_data
        
    def simulateIOGeneticCircuitResponse():
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
        u2 = 1;

        del = 1;
        gam = 1;



        kap = 1000;
        D = 10;
        D2 = 10;
        K_k = 0.1;
        K_l = 0.1;
        d = 100;
        """
        rm = te.loada(reduced_model)
        rm_data = rm.simulate(0,8,2000)
        rm.plot(title="CRISPRa Modality I Model", xlabel= "Time (sec)", ylabel= "Concentration")
        return rm_data
        

    def changeMachineryConcentration(dCas9=1, Activator=1, *args):
        """ changeMachinery Concentration
        - Changes the dCas9 and MCP-SoxS activator machinery
        Args:
            dCas9 (int, optional): dCas9 protein concentration. Defaults to 1.
            Activator (int, optional): MCP-SoxS protein complex concentration. Defaults to 1.
            args: Array for K values that influence machinery concentration
        """
        return "Changing machinery concentration"

    def setCompetitorCircuits(value=1):
        """setCompetitorCircuits
        - This function changes the tellurium model depending on the value supplied to increase the number of competitors
        Args:
            value (int, optional): _description_. Defaults to 1.
        """
        print("Set competitor circuits")

    def setTargetCircuit(value=1):
        """SetTargetCircuit, Define the target DNA you're targeting, this should change the parameter of DNA being targeted

        Args:
            value (int, optional): _description_. Defaults to 1.
        """
        print("Define target circuit")

    def changeInputResponseRange(responseRange):
        print("Changing the input response range")

    def extractSteadyStateValues():
        print("Get steady state")
