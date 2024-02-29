# setup.py
from setuptools import setup, find_packages

setup(
    name='mcu_communication_tcp',
    version='1.0.0',
    description='Python package for MCU communication tcp mcu_protocol',
    packages=find_packages(),
    install_requires=["flatbuffers","mcu_communication_protocol","twisted","numpy"]
)
