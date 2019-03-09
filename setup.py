import os
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="wild-nlp",
    version="0.0.3",
    author="Dominika Basaj, Barbara Rychalska, Alicja Gosiewska, Adam Słucki",
    author_email="adam.slucki@gmail.com",
    description=("Text aspects for nlp models"),
    license="BSD",
    url="https://github.com/MI2DataLab/WildNLP",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ]
)
