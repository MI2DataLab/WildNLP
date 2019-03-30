from __future__ import print_function

from io import open
import os
import random

from .base import Aspect


class SentimentMasking(Aspect):
    """This aspect reflects attempts made by Internet users
    to mask profanity or hate speech in online forums to evade moderation.
    We perform masking (replacing random, single character with for example an asterisk)
    of negative (or positive for completeness) words from Opinion Lexicon:
    http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html

    *All words that are listed will be transformed.*

    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, char='*', use_positive=False, seed=42):
        """
        :param char: A character that will be used to mask words.

        :param use_positive: If True positive (instead of negative)
                             words will be masked.

        :param seed: Random seed.
        """

        if isinstance(char, str) and len(char) == 1:
            self._char = char
        else:
            self._char = '*'
            print('Only single characters should be used for masking.')

        filename = 'negative_words.txt'
        if use_positive:
            filename = 'positive_words.txt'
        self._sentiment_words = self._sentiment_words(filename)

        random.seed(seed)

    def __call__(self, sentence):
        tokens = self._tokenize(sentence)

        modified_tokens = self._transform_tokens(tokens)

        return self._detokenize(modified_tokens)

    def _transform_tokens(self, tokens):

        modified = []
        for token in tokens:
            if token.lower() in self._sentiment_words:
                ind = random.randint(0, len(token)-1)
                token = token[:ind] + self._char + token[ind+1:]
                # TODO: Appending a char instead of replacing is
                #   not implemented as it violates description
                #   from the paper.

            modified.append(token)

        return modified

    @staticmethod
    def _sentiment_words(filename):

        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, 'auxiliary', filename)

        with open(path, 'r', encoding='utf-8') as f:
            words = f.readlines()

        return [word.strip('\n') for word in words
                if word[0] != ';' and word != '\n']
