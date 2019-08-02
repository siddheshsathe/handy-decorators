from setuptools import setup, find_packages
from src.decorators import __version__

with open('README.md', 'r') as description_file:
    long_description = description_file.read()

setup(
    name='handy-decorators',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=__version__,
    description='Handy decorators for day-to-day use!',
    py_modules=['decorators'],
    package_dir={'': 'src'},
    install_requires=['logging'],
)
