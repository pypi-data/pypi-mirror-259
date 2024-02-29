from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
name='PyRandomLoop',
version='0.1.1',
author='Lorenzo Gregoris',
author_email='lorenzo.gregoris@gmail.com',
description='The package provides a simulation framework for a random loop model in statistical mechanics, including initialization, simulation, and visualization capabilities. The core of the simulation is the class `stateSpace`. Features include performance optimizations, execution logging, and statistics calculation, alongside visualization tools for detailed analysis. Ideal for researchers and students in physics and related fields.',
long_description=long_description,
long_description_content_type = 'text/markdown' ,
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.11.8',
)