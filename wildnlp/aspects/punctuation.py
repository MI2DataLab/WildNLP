from __future__ import print_function, division

import random

from .base import Aspect


class Punctuation(Aspect):
    """Randomly adds or removes specified punctuation marks.
    The implementation guarantees that punctuation marks won't be
    appended to the original ones or won't replace them after removal.

    With default settings all occurrences of the specified punctuation
    mark will be removed.

    - Example::

        Sentence, have a comma.

        Possible transformations:
        - Sentence have, a comma.
        - Sentence, have, a, comma.

        Impossible transformations:
        - Sentence,, have a comma.

    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, char=',', add_percentage=0, remove_percentage=100, seed=42):
        """

        :param char: Punctuation mark that will be removed or
            added to sentences.

        :param add_percentage: Max percentage of white spaces in a sentence
            to be prepended with punctuation marks.

        :param remove_percentage: Max percentage of existing punctuation marks
            that will be removed.

        :param seed: Random seed.
        """

        if add_percentage >= 1:
            add_percentage /= 100.
        if remove_percentage >= 1:
            remove_percentage /= 100.

        if isinstance(char, str) and len(char) == 1:
            self._char = char
        else:
            self._char = ','
            print('Only single characters can be used as punctuation marks.')

        self._add_percentage = add_percentage
        self._remove_percentage = remove_percentage

        random.seed(seed)

    def __call__(self, sentence):

        modified_sentence = self._modify_punctuation(sentence)

        return modified_sentence

    def _modify_punctuation(self, sentence):
        punctuation_idx = []
        space_idx = []
        for i, char in enumerate(sentence):
            if char == self._char:
                punctuation_idx.append(i)
            elif char == ' ':
                try:
                    # Prevent doubling punctuation marks.
                    if i == punctuation_idx[-1] + 1:
                        continue
                except IndexError:
                    pass

                space_idx.append(i)

        random.shuffle(punctuation_idx)
        random.shuffle(space_idx)

        selected_punctuation = \
            sorted(punctuation_idx[:int(len(punctuation_idx) * self._remove_percentage)])
        selected_space = \
            sorted(space_idx[:int(len(space_idx) * self._add_percentage)])

        modified = ""
        for i, char in enumerate(sentence):
            if i in selected_punctuation:
                char = ''
            elif i in selected_space:
                char = self._char + ' '

            modified += char

        return modified
