import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="yt_data",
    version="1.0",
    author="Dominika Basaj, Adam Słucki",
    author_email="adam.slucki@gmail.com",
    description=("Wrapper for youtube data API"),
    license="BSD",
    packages=['yt_data'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ]
)
