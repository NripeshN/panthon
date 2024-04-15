import setuptools
from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")


def _strip(line):
    return line.split(" ")[0].split("#")[0].split(",")[0]


setup(
    name="panthon",
    version="0.2.4",
    author="Nripesh",
    author_email="Nripesh14@gmail.com",
    description=(
        "Panthon employs sophisticated methods to replicate different cyber threats,"
        " offering a dynamic solution to proactively address the constantly shifting"
        " realm of cybersecurity risks. Our goal is to help build more resilient and"
        " secure systems through a deeper understanding and anticipation of potential"
        " vulnerabilities."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=setuptools.find_packages(),
    package_data={"panthon": ["*"]},
    install_requires=[
        _strip(line)
        for line in open("requirements.txt", "r", encoding="utf-8").readlines()
    ],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
    ],
    license="Apache Software License",
)
