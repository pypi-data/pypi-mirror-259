from setuptools import setup, find_packages

setup(
    name='biocomet',
    version='0.1.02',
    author='Nicolas Ruffini',
    author_email='nicolas.ruffini@lir-mainz.de',
    description='A brief description of the biocomet package',
    url='https://github.com/NiRuff/COMET/tree/master_kegg',  # Optional
    package_dir={'': 'biocomet'},
    packages=find_packages(where='biocomet'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
