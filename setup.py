from setuptools import setup, find_packages

# Initializes the project after cloning

# Initialize README file
with open("README.md", "r") as f:
    file_description = f.read()

REQUIREMENTS = ['numpy', 'tellurium', 'pandas']

short_description = 'A CRISPRai modeling package for modeling large-scale genetic circuits'

setup(
        name='CRISPRAICIRCUITMODELING',
        version= '0.0.2',
        author= 'Tommy G. Primo',
        author_email= 'tprimo@uw.edu',
        url='https://github.com/TommyGPrimo/CRISPRaiCircuitsModeling',
        description= short_description,
        long_description= file_description,
        long_description_content_type= 'text/markdown',
        packages=find_packages(),
        package_dir={'crisprai_model': 'crisprai_model'},
        install_requirements = REQUIREMENTS,
        include_package_data= True,
        classifiers=['Development Status :: Alpha', 'Intended Audience :: Science/Research', 'Topic :: Scientific/Engineering', 'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python :: 3.9', 'Programming Language :: Python :: 3.10', "Programming Language :: Python :: 3.11"],
        extra_require={"dev":['pytest>=7.0', 'twine>=4.0.2'],}
    )