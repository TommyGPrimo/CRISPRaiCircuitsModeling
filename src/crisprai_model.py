
# Import functions
import tellurium as te
import numpy as np
import matplotlib.pyplot as plt

import logging

# Define CRISPRai model class
class crisprai_model:
    
    def checkGeneticCircuitComponents():
        """ checkGeneticCircuitComponents
        - Prints out the values of the CRISPRai components including genetic circuit components for review by the user
        """
        print("Checking Genetic circuit components")

    def simulateGeneticCircuits():
        """ simulateGeneticCircuits
        - Generates a tellurium simulation of the steady state response of the input
        """
        print("Simulating genetic circuits")

    def changeMachineryConcentration(dCas9=1, Activator=1, *args):
        """ changeMachinery Concentration
        - Changes the dCas9 and MCP-SoxS activator machinery
        Args:
            dCas9 (int, optional): dCas9 protein concentration. Defaults to 1.
            Activator (int, optional): MCP-SoxS protein complex concentration. Defaults to 1.
            args: Array for K values that influence machinery concentration
        """
        print("Changing machinery concentration")

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
