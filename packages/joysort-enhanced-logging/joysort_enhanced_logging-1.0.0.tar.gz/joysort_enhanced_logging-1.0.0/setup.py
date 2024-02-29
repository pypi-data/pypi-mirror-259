# setup.py
from setuptools import setup, find_packages

setup(
    name='joysort_enhanced_logging',
    version='1.0.0',
    description='Python package for joysort_enhanced_logging',
    packages=find_packages(),
    install_requires=["colorama","mcu_communication_protocol"]
)
