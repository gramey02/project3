from setuptools import find_packages
from setuptools import setup

setup(
    name= 'mst',
    version= '0.0.1',
    author= 'Grace Ramey',
    author_email= 'Grace.Ramey@ucsf.edu',
    packages= find_packages(),
    description= 'Finds a minimum spanning tree for a connected adjacency matrix',
	install_requires= ['pytest', 'typing', 'sklearn.metrics', 'numpy']
)