# setup.py
from setuptools import setup, find_packages

setup(
    name='mcu_communication_protocol',
    version='1.0.0',
    description='Python package for MCU communication mcu_protocol',
    packages=find_packages(),
    include_package_data=True,  # Key change
    package_data={
        'mcu_communication_protocol': ['assets/*'],  # Include all assets in the 'assets' directory
    },
    install_requires=["flatbuffers"]
)
