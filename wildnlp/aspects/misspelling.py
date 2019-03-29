import json
import os
import random

from .base import Aspect


class Misspelling(Aspect):
    """Misspells words appearing in the Wikipedia list of
    **commonly misspelled English words** (default):
    https://en.wikipedia.org/wiki/Commonly_misspelled_English_words

    .. tip:: You can use **homophones** instead:
        https://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/Homophones

    If a word has more then one common misspelling, the replacement
    is selected randomly.

    *All words that have any misspellings listed will be replaced.*

    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, use_homophones=False, seed=42):
        """
        :param use_homophones: If True list of homophones will be used
                               to replace words.

        :param seed: Random seed.
        """

        filename = 'misspellings.json'
        if use_homophones:
            filename = 'homophones.json'
        self._misspellings = self._load_misspellings(filename)

        random.seed(seed)

    def __call__(self, sentence):
        tokens = self._tokenize(sentence)

        modified_tokens = self._transform_tokens(tokens)

        return self._detokenize(modified_tokens)

    def _transform_tokens(self, tokens):

        modified = []
        for token in tokens:
            if token.lower() in self._misspellings:

                modified_token =\
                    random.choice(self._misspellings[token.lower()])
                if token[0].isupper():
                    modified_token = self._capitalize(modified_token)

                token = modified_token
            modified.append(token)

        return modified

    @staticmethod
    def _load_misspellings(filename):

        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, 'auxiliary', filename)
        with open(path, 'r') as f:
            mistakes = json.load(f)

        return mistakes

    @staticmethod
    def _capitalize(token):
        try:
            return token[0].upper() + token[1:]
        except IndexError:
            return token
