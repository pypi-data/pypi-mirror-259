import os
from setuptools import setup, find_packages

VERSION = os.getenv('PYAGET_VERSION')
DESCRIPTION = "Piaget's FUCs filler"
LONG_DESCRIPTION = 'Opytimal is a Python/FEniCS framework that have the main goal solve Optimal Control problems considering multiple and mixed controls based to linear and nonlinear PDEs, in addition to can also solve PDEs simply and clearly'

setup(
    name="pyaget_fucs",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Natanael Quintino",
    author_email="natanael.quintino@ipiaget.pt",
    license='CC0 1.0 Universal',
    packages=find_packages(
        include=['pyaget_fucs', 'pyaget_fucs.*']
        ),
    install_requires=[
        "pdflatex", "langchain_openai"
    ],
    keywords='automation, curricular unit, FUC, piaget',
    classifiers= [
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
