"""
Setup file for the Panthon package. Specifies package details and dependencies.
"""
from setuptools import setup, find_packages

# Read in requirements.txt with specified encoding
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='panthon',
    version='0.1.0',
    url='https://github.com/yourusername/panthon',
    author='Author Name',
    author_email='author@gmail.com',
    description='A Machine Learning-powered Cybersecurity Attack Simulation Library',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)