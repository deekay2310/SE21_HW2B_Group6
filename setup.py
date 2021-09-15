from setuptools import setup, find_packages

setup(
    name='Calculator',
    version='1.0.0',
    packages=find_packages(),
    license='none',
    description='A simple calculator for basic mathematical operations',
    author='Dev, Prakruthi, Radhika, Rohan, Sunidhi',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
