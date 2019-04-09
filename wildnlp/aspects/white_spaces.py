import random

from .base import Aspect


class WhiteSpaces(Aspect):
    """Randomly adds or removes specified extended white spaces.
    The implementation guarantees that any chars won't be
    appended to the original sentence or won't replace them after removal.

    With default settings all occurrences of the specified punctuation
    mark will be removed.

    - Example::

        Sentence     havea com  ma.

        Possible transformations:
        - Sente nce have a comma.
        - Sentence     have acomma.

    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, white_spaces=" \t\n", add_percentage=0, remove_percentage=100, seed=42):
        """

        :param white_spaces: A string contaning all used white spaces characters.

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

        # TODO Are those all white spaces?
        self._white_spaces = white_spaces
        self._add_percentage = add_percentage
        self._remove_percentage = remove_percentage

        random.seed(seed)

    def __call__(self, sentence):

        modified_sentence = self._modify_white_spaces(sentence)

        return modified_sentence

    def _modify_white_spaces(self, sentence):

        char_idx = []
        space_idx = []

        for i, char in enumerate(sentence):
            if char in self._white_spaces:
                space_idx.append(i)
            else:
                char_idx.append(i)

        random.shuffle(char_idx)
        random.shuffle(space_idx)

        selected_char = \
            sorted(char_idx[:int(len(char_idx) * self._add_percentage)])
        selected_space = \
            sorted(space_idx[:int(len(space_idx) * self._remove_percentage)])

        modified = ""
        prev_idx = 0
        added = False

        for i, char in enumerate(sentence):
            if i in selected_char:
                modified += sentence[prev_idx:i] + random.choice(self._white_spaces)
                prev_idx = i
                added = True
            elif i in selected_space:
                modified += sentence[prev_idx:i]
                prev_idx = i+1
                added = True
            else:
                modified += sentence[prev_idx:i+1]
                prev_idx = i+1
                added = True

        if added:
            modified += sentence[-1]

        return modified
