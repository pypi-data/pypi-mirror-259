from setuptools import setup, find_packages
import os

version = os.getenv('VERSION', '0.1.0') # Usa la versión del tag o 0.1 como predeterminado

setup(
    name='brian_lib',
    version=version,
    packages=find_packages(),
    install_requires=[
        "pandas==2.1.0"
    ],
    python_requires='>=3.7'
)