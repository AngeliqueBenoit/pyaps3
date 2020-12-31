from setuptools import setup, find_packages

setup(
    name='pyaps3',
    version='1.0',
    description="Python based Atmospheric Phase Screen Estimation",
    url="https://github.com/AngeliqueBenoit/pyaps3",
    author="Angelique Benoit, Romain Jolivet",
    author_email="insar@geologie.ens.fr",
    packages=find_packages(),
    package_data={'': ['*.cfg']},
    include_package_data=True,
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'cdsapi'
    ]
)