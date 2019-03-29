import random

from .base import Aspect


class Swap(Aspect):
    """Randomly swaps two characters within a word, excluding punctuations.
    It's possible that the same two characters will be swapped, so
    the word won't be changed, for example `letter` can become `letter`
    after swapping.

    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, transform_percentage=100, seed=42):
        """

        :param transform_percentage: Maximum percentage of words in a
            sentence that should be transformed.

        :param seed: Random seed.
        """

        if transform_percentage > 1:
            transform_percentage /= 100.

        self._transform_percentage = transform_percentage

        random.seed(seed)

    def __call__(self, sentence):
        tokens = self._tokenize(sentence)

        modified_tokens = self._swap_characters(tokens)

        return self._detokenize(modified_tokens)

    def _swap_characters(self, tokens):

        # TODO: It's different than example in the paper
        #       where two letter words are also included.
        tokens_filtered = [i for i, token in enumerate(tokens)
                           if len(token) > 2]

        random.shuffle(tokens_filtered)
        selected_tokens =\
            sorted(tokens_filtered[:self._percentage_to_number(len(tokens))])

        modified = []
        for i, token in enumerate(tokens):
            if i in selected_tokens:
                idx_letter_first = random.randint(1, len(token) - 2)
                token = token[:idx_letter_first]\
                    + token[idx_letter_first + 1]\
                    + token[idx_letter_first]\
                    + token[idx_letter_first + 2:]

            modified.append(token)

        return modified

    def _percentage_to_number(self, num_tokens):
        return int(self._transform_percentage * num_tokens)

