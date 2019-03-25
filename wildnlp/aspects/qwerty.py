import json
import os
import random

from .base import Aspect


class QWERTYSwapper(Aspect):
    """Simualtes errors made while writing on a QWERTY-type keyboard.
    Characters are swapped with their neighbors on the keyboard.

    .. warning:: Uses random numbers, default seed is 42.
    """

    def __init__(self, num_words_to_swap=1, seed=42):
        """

        :param num_words_to_swap: Maximum number of words in a sentence
                                  that should be transformed. Defaults to one.

        :param seed: Random seed.
        """

        # TODO According to the original implementation
        #     it seem's that the variable should default to 1.
        self._num_words_to_swap = num_words_to_swap
        self._qwerty_mistakes = self._load_qwerty_mistakes()

        random.seed(seed)

    def __call__(self, sentence):
        tokens = self._tokenize(sentence)

        modified_tokens = self._transform_tokens(tokens)

        return self._detokenize(modified_tokens)

    def _transform_tokens(self, tokens):

        # TODO Differently to other aspects, here
        #    we don't filter out punctuations etc.
        tokens_idx = list(range(len(tokens)))
        random.shuffle(tokens_idx)

        selected_tokens = sorted(tokens_idx[:self._num_words_to_swap])

        modified = []
        for i, token in enumerate(tokens):
            if i in selected_tokens:
                token = self._transform_token(token)
            modified.append(token)

        return modified

    def _transform_token(self, token):

        try:
            selected_char = random.choice(token)
            possible_mistakes = self._qwerty_mistakes[selected_char.lower()]
            mistake = random.choice(possible_mistakes)
            occurrences = random.randint(1, token.count(selected_char))
            transformed_token = token.replace(selected_char, mistake, occurrences)

        except (IndexError, KeyError):
            transformed_token = token

        return transformed_token

    @staticmethod
    def _load_qwerty_mistakes():

        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, 'auxiliary', 'qwerty.json')
        with open(path, 'r') as f:
            mistakes = json.load(f)

        return mistakes




