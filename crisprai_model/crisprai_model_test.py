""" CRISPRai_model testing file
"""

# Imports
import unittest
from crisprai_model import crisprai_model as cai

class crisprai_model_test(unittest.TestCase):
    
    def test_crisprai_model(self):
        self.assertEquals()
    
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


