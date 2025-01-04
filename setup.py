from setuptools import setup

setup(
    name='parser_of-currencies_rbk',
    version='1.0',
    description='A useful module',
    author='CHT VENDETTA',
    packages=['parser_of_currencies_rbk'],  # same as name
    install_requires=['beautifulsoup4',
                      'certifi',
                      'charset-normalizer',
                      'idna',
                      'requests',
                      'soupsieve',
                      'urllib3'],  # external packages as dependencies
)