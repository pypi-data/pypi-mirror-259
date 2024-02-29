# setup.py
from setuptools import setup, find_packages

setup(
    name='mcu_communication',
    version='1.0.0',
    description='Python package for MCU communication protocol',
    packages=find_packages(),
    install_requires=["flatbuffers","flask","flask_restx"]
)
