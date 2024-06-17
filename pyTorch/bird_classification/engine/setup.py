#from setuptools import setup, find_packages
import sys

sys.path.append("/opt/conda/envs/py-project/lib/python3.8/site-packages")
from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Model engine package"
LONG_DESCRIPTION = "Model engine package for pyTorch"

setup(
    name='engine',
    version = VERSION,
    author="Ted Li",
    packages = find_packages(),
    keywords=['python', 'pytorch', 'engine']
)