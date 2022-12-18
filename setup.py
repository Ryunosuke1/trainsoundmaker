from setuptools import setup, find_packages
##from glab import glab
##from os.path import join
##from os.path import splittext
from distutils.core import setup
##def read_requirements():
    ##reqs_path = os.path.join('.','requirements.txt')
    ##with open(reqs_path, 'r') as f:
        ##equirements = [line.rstrip() for line in f]
        ##return requirements
setup(name="trainsoundmaker", version="0.0.1", description="trainsoundmakeingcode", long_description="readme", author="Ryunosuke", package=['view'], install_requires=["numpy>=1.2", "soundfile>=0.11.0", "scipy>=1.9.3", "pyrubberband>=0.3.0", "click>=8.1.3"])

