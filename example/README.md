# Evaluation of BiDAF robustness.
This is an example of robustness evaluation. We use trained [BiDAF](https://arxiv.org/abs/1611.01603) model
and [SQuAD (v.1)](https://rajpurkar.github.io/SQuAD-explorer/) dataset to measure F1 scores under
different levels of text corruption severity. 

## Evaluation details
The full script is available in this repository, see the [evaluation.py](evaluation.py).
Below we provide excerpts from it.

## Loading resources
```python
import allennlp
import requests

data = requests.get('https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json').json()

BiDAF =\
    allennlp.predictors.predictor.Predictor.from_path(
        "https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")
```


## Notes
The script downloads resources from third parties.
It may break any time when those resources will be no longer available.