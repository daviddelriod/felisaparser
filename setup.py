from setuptools import setup
setup(
    name = 'felisaparser',
    version = '1.0.0',
    description = 'This package contains a function to directly parse a excel file into a csv file',
    author = 'Adrián Martínez, David Del Río',
    url = 'https://github.com/daviddelriod/felisaparser',
    keywords = 'xlsx parser',
    install_requires = [
        'pandas',
        ],
)