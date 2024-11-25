from setuptools import setup

# Initializes the project after cloning

# Initialize README file
with open("README.md", "r") as f:
    file_description = f.read()

REQUIREMENTS = []

short_description = 'A CRISPRai modeling package for modeling large-scale genetic circuits'

def callSetup(requirements):
    setup(
        name='CRISPRAICIRCUITMODELING',
        version= '0.1',
        author= 'Tommy G. Primo',
        author_email= 'tprimo@uw.edu',
        url='https://github.com/TommyGPrimo/CRISPRaiCircuitsModeling',
        description= short_description,
        long_description= file_description,
        long_description_content_type= 'text/markdown',
        packages=['crisprai_model'],
        package_dir={'crisprai_model': 'crisprai_model'},
        install_requirements = requirements,
        include_package_data= True,
        classifiers=['Development Status :: Alpha', 'Intended Audience :: Science/Research', 'Topic :: Scientific/Engineering', 'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python :: 3.9', 'Programming Language :: Python :: 3.10', "Programming Language :: Python :: 3.11"]
    )

if __name__ == "__main__":
    callSetup(REQUIREMENTS)
