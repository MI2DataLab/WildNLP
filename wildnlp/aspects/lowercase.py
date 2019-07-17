import random

from .base import Aspect


class LowerCase(Aspect):
    """Randomly lowercases the dataset

    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, words_percentage=50, seed=42):
        """

        :param words_percentage: Percentage of the words in the dataset which needs to be lowercased.
                                 Defaults to 0.5.

        :param seed: Random seed.
        """

        if words_percentage >= 1:
            words_percentage /= 100.

        random.seed(seed)

    def __call__(self, sentence):
        tokens = self._tokenize(sentence)
        lowercased_tokens = self._lowercase_tokens(tokens)
        return self._detokenize(lowercased_tokens)

    @staticmethod
    def _lowercase_tokens(tokens):

        modified = []
        for token in tokens:
            token = token.lower()
            modified.append(token)
        return modified

    @staticmethod
    def _capitalize(token):
        try:
            return token[0].upper() + token[1:]
        except IndexError:
            return token
