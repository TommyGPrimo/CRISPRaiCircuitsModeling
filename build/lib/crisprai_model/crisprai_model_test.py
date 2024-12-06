""" CRISPRai_model testing file
"""

# Imports
import unittest
from crisprai_model import crisprai_model as cai

# Initialize the package and model
cai_circuit = cai()
cai_model = cai_circuit.get_crispra_model() # Test this by making sure you get a string returned

# Plot model
cai_simulation = cai_circuit.simulate_crispra_model(cai_model, time=8) # Test this to see if you're getting the array dynamics for your model...can adjust the time
#cai_circuit.plot_crispra_model(cai_simulation[0])

# Change concentration of machinery
updated_model = cai_circuit.change_concentration_of_machinery(cai_simulation[0], dcas_9=2, guide=1, target=1)
#cai_circuit.plot_crispra_model(updated_model)

# IO visualization
io_model = cai_circuit.get_io_model()
io_simulation = cai_circuit.simulate_io_model(io_model)

cai_circuit.visualize_io_response(io_simulation[0], 8, [10,1000]) # Comparing CRISPRa complex and 10x CRISPRa complex, for how much inducer is needed``

class crisprai_model_test(unittest.TestCase):
    
    def test_crisprai_model(self):
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
        self.assertEquals(model,cai_model,"Model is correct")
        
    def test_simulation(self):
        self.assertIsInstance(cai_simulation, list, "The function does not return an array (list).")
    
    def test_updated_model_returned(self):
        self.assertIsNotNone(updated_model, "The function returned None.")
    
    def test_return_io_model(self):
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
        self.assertEquals(reduced_model,io_model,"Model is correct")
    def test_io_simulation(self):
        self.assertIsInstance(io_simulation, list, "The function does not return an array (list).")
        


