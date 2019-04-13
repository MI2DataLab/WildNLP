import random

from .base import Aspect


class AddSubString(Aspect):
    """Randomly adds specified extended sub-strings.
    The implementation guarantees that punctuation marks won't be replaced them after removal.
    The result string will be longer than the original/input one.

    With default settings all occurrences of the specified punctuation
    mark will be removed.

    - Example::

        Sentence have a comma.

        Possible transformations:
        - Sentence have a comma.
        - Sentence have a comma.

    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, add_string="", add_percentage=10, seed=42):
        """

        :param add_string: String with extended tokens that will be added to sentences.

        :param add_percentage: Max percentage of substrings in a sentence
            to be prepended with punctuation marks.

        :param seed: Random seed.
        """

        if add_percentage >= 1:
            add_percentage /= 100.

        self._add_string = add_string

        self._add_percentage = add_percentage

        random.seed(seed)

    def __call__(self, sentence):

        modified_sentence = self._modify_add_string(sentence)

        return modified_sentence

    def _modify_add_string(self, sentence):

        selected_string_starts = [i for i, _ in enumerate(sentence)]
        random.shuffle(selected_string_starts)

        selected_string_starts = \
            sorted(selected_string_starts[:self._percentage_to_num(
                sentence, self._add_percentage)])

        modified = ""
        prev_idx = 0
        added = False

        for i, char in enumerate(sentence):
            if i in selected_string_starts:
                modified += sentence[prev_idx:i] + self._add_string
                prev_idx = i
                added = True
            else:
                modified += sentence[prev_idx:i + 1]
                prev_idx = i + 1
                added = False

        if added:
            modified += sentence[-1]

        return modified

    @staticmethod
    def _percentage_to_num(array, percentage):
        # Ensure that at least one item will be transformed.
        if percentage == 0:
            return 0
        return max(1, int(len(array) * percentage))
