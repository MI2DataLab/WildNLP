[![Documentation Status](https://readthedocs.org/projects/nlp-demo/badge/?version=latest)](https://nlp-demo.readthedocs.io/en/latest/?badge=latest)

![alt wildnlp-logo](logo.png)  

Corrupt an input text to test NLP models' robustness.
For details refer to https://nlp-demo.readthedocs.io

## Installation
`pip install wild-nlp`

## Usage
```python
from wildnlp.aspects import Reverser, PigLatin
from wildnlp.aspects.utils import compose
from wildnlp.datasets import SampleDataset

# Create a dataset object and load the dataset
dataset = SampleDataset()
dataset.load()

# Crate a composed corruptor function.
# Functions will be applied in the same order they appear.
composed = compose(Reverser(), PigLatin())

# Apply the function to the dataset
modified = dataset.apply(composed)
```
