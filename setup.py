import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="wild-nlp",
    version="0.0.1",
    author="Dominika Basaj, Barbara Rychalska, Alicja Gosiewska, Adam Słucki",
    author_email="adam.slucki@gmail.com",
    description=("Text aspects for nlp models"),
    license="BSD",
    url="https://github.com/MI2DataLab/WildNLP",
    packages=['wildnlp'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ]
)
