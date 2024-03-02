from setuptools import find_packages
from setuptools import setup


description = "Book a session with volunteer to discuss programming"


with open("README.md") as file:
    long_description = file.read()


with open("requirements.txt") as file:
    requirements = file.read()


setup(
    name="dbn4-clinic",
    version="0.4.0",
    author="DBN-04-2023",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["commands", "utils"]),
    python_requires = ">=3.10",
)
