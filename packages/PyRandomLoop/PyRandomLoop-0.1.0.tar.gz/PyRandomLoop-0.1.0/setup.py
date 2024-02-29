from setuptools import setup, find_packages

setup(
name='PyRandomLoop',
version='0.1.0',
author='Lorenzo Gregoris',
author_email='lorenzo.gregoris@gmail.com',
description='The package provides a simulation framework for a random loop model in statistical mechanics, including initialization, simulation, and visualization capabilities. The core of the simulation is the class `stateSpace`. Features include performance optimizations, execution logging, and statistics calculation, alongside visualization tools for detailed analysis. Ideal for researchers and students in physics and related fields.',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.11.8',
)