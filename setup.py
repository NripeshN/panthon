"""Setup file for the Panthon package.

Specifies package details and dependencies.
"""
from setuptools import setup, find_packages
from pathlib import Path


requirements = [
    "torch",
    "scapy",
    "netifaces",
    "bs4",
    "tld",
    "fuzzywuzzy",
    "requests",
    "twisted",
]

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="panthon",
    version="0.1.14",
    url="https://github.com/nripeshn/panthon",
    author="Nripesh Niketan",
    author_email="nripesh14@gmail.com",
    description="A Cybersecurity Attack Simulation Library",
    long_description=long_description,
    packages=find_packages(),
    package_data={"panthon": ["data/*.txt"]},
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
