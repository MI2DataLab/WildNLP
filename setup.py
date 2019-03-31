import os
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="wild-nlp",
    version="1.0.1",
    author="Dominika Basaj, Barbara Rychalska, Alicja Gosiewska, Adam Słucki",
    author_email="adam.slucki@gmail.com",
    description=("Text aspects for nlp models"),
    license="BSD",
    url="https://github.com/MI2DataLab/WildNLP",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Text Processing",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'numpy',
        'num2words'
    ]
)
