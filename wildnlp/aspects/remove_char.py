import math
import random

from .base import Aspect


class RemoveChar(Aspect):
    """Randomly removes characters from words.

    .. Note:: Note that you may specify white space as a character to be removed
              but it'll be processed differently.
    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, char=None, words_percentage=50,
                 characters_percentage=10, seed=42):
        """

        :param words_percentage: Percentage of words in a
            sentence that should be transformed. Nevertheless, always at
            least single word should be transformed..

        :param characters_percentage: Percentage of characters in a
            word that should be transformed. Nevertheless, always at
            least single character should be removed.

        :param char: If specified only that character will be randomly removed.
             The specified character can also be a white space.

        :param seed: Random seed.
        """

        if words_percentage > 1:
            words_percentage /= 100.

        if characters_percentage > 1:
            characters_percentage /= 100.

        self._words_percentage = words_percentage
        self._characters_percentage = characters_percentage
        self._char = char

        random.seed(seed)

    def __call__(self, sentence):

        if self._char == ' ':
            return self._process_white_space(sentence)

        tokens = self._tokenize(sentence)
        modified_tokens = self._remove_characters(tokens)

        return self._detokenize(modified_tokens)

    def _remove_characters(self, tokens):

        # TODO: I think that punctuation marks etc. should
        #     be excluded.
        tokens_filtered = [i for i, token in enumerate(tokens)
                           if token.isalpha() or token.isdigit()]
        random.shuffle(tokens_filtered)

        selected_tokens =\
            sorted(tokens_filtered[:self._percentage_to_num(
                tokens_filtered, self._words_percentage)])

        modified = []
        for i, token in enumerate(tokens):
            if i in selected_tokens:

                if self._char:
                    token = token.replace(self._char, '',
                                          self._percentage_to_num(
                                              token,
                                              self._characters_percentage))
                else:
                    # TODO: Here's the change,
                    #  now all the characters are selected randomly.
                    selected_chars = [i for i, _ in enumerate(token)]
                    random.shuffle(selected_chars)

                    selected_chars =\
                        sorted(selected_chars[:self._percentage_to_num(
                            token, self._characters_percentage)])

                    modified_token = ""
                    for j, char in enumerate(token):
                        if j in selected_chars:
                            char = ''
                        modified_token += char

                    token = modified_token

            modified.append(token)

        return modified

    def _process_white_space(self, sentence):
        occurrences = int((sentence.count(' ') * self._words_percentage))

        return sentence.replace(' ', '', occurrences)

    @staticmethod
    def _percentage_to_num(array, percentage):
        if percentage == 0:
            return 0
        # Ensure that at least one item will be transformed.
        return max(1, int(len(array) * percentage))





