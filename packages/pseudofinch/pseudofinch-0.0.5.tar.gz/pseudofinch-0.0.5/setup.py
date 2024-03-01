from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.5'
DESCRIPTION = 'Finch robot 2.0 functions in python'
LONG_DESCRIPTION = 'An emulation library of the Finch robot 2.0 functions in python'

# Setting up
setup(
    name="pseudofinch",
    version=VERSION,
    author="Quarksay",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'robot', 'finch', 'automation', 'classroom', 'school'],
)