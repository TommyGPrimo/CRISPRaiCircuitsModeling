"""__init__ file: initializer should contain all necessary information to run package
"""

# Import functions
import logging
import pdb

# List the names of all modules used for working with package, version
__all__ = ["crisprai_model_test"]
__version__ = "1.0.0"
__name__ = "CRISPRai_Genetic_Circuits_Model"

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("Run Sucessfully!")
