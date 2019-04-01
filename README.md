[![Documentation Status](https://readthedocs.org/projects/nlp-demo/badge/?version=latest)](https://nlp-demo.readthedocs.io/en/latest/?badge=latest)

![alt wildnlp-logo](logo.png)  

Corrupt an input text to test NLP models' robustness.  
For details refer to https://nlp-demo.readthedocs.io

## Installation
`pip install wild-nlp`

## Supported aspects
All together we defined and implemented 11 aspects of text corruption.

1. **Articles**
   
   Randomly removes or swaps articles into wrong ones.

2. **Digits2Words**

   Converts numbers into words. Handles floating numbers as well.

3. **Misspellings**

   Misspells words appearing in the Wikipedia list of:
    **commonly misspelled English words**  
    **homophones**

4. **Punctuation**

   Randomly adds or removes specified punctuation marks.

5. **QWERTY**

   Simulates errors made while writing on a QWERTY-type keyboard.

6. **RemoveChar**

   Randomly removes:  
   **characters** from words or  
   **white spaces** from sentences

7. **SentimentMasking**

   Replaces random, single character with for example an asterisk)
   in:  
   **negative** or  
   **positive** words from Opinion Lexicon:    
   http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html

8. **Swap**

   Randomly swaps two characters within a word, excluding punctuations.

```diff
- All aspects can be chained together with the wildnlp.aspects.utils.compose function.
```

## Supported datasets
Aspects can be applied to any text. Below is the list of datasets for which we already implemented processing pipelines. 

1. **CoNLL**

   The CoNLL-2003 shared task data for language-independent named entity recognition.

2. **IMDB**

   The IMDB dataset containing movie reviews for a sentiment analysis. The dataset consists of 50 000 reviews of two classes, negative and positive.

3. **SNLI**

   The SNLI dataset supporting the task of natural language inference.

4. **SQuAD**

   The SQuAD dataset for the Machine Comprehension problem.

## Usage
```python
from wildnlp.aspects.dummy import Reverser, PigLatin
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
