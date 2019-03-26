import random

from .base import Aspect


class RemoveChar(Aspect):
    """Randomly removes characters from words.

    .. warning:: Uses random numbers, default seed is 42.
    """

    def __init__(self, char=None, transform_percentage=100, seed=42):
        """

        :param transform_percentage: Maximum percentage of words in a
            sentence that should be transformed. Punctuation marks and
            special characters are ignored.

        :param char: If specified only that character will be randomly removed.
             The specified character can also be a white space.

        :param seed: Random seed.
        """

        if transform_percentage > 1:
            transform_percentage /= 100.

        self._transform_percentage = transform_percentage
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
            sorted(tokens_filtered[:self._percentage_to_number(
                len(tokens_filtered))])

        modified = []
        for i, token in enumerate(tokens):
            if i in selected_tokens:

                if self._char:
                    selected_char = self._char
                else:
                    selected_char = random.choice(token)

                try:
                    occurrences =\
                        random.randint(1, token.count(selected_char))
                    token = token.replace(selected_char, '', occurrences)
                except ValueError:
                    pass

            modified.append(token)

        return modified

    def _process_white_space(self, sentence):
        occurrences = self._percentage_to_number(sentence.count(' '))

        return sentence.replace(' ', '', occurrences)

    def _percentage_to_number(self, num_tokens):
        return int(self._transform_percentage * num_tokens)




