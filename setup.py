from setuptools import setup,find_packages

setup(
    name="trainsoundmaker"
    version="0.0.1"
    description="trainsoundmakeingcode"
    long_description='readme'
    author=''
    package=['view']
    )
def read_requirements():
    reqs_path = os.path.join('.','requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
        return requirements
