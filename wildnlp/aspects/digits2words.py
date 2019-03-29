import re

from num2words import num2words

from .base import Aspect


class Digits2Words(Aspect):
    """Converts numbers into words.
    Handles floating numbers as well.

    *All numbers will be converted*
    """

    def __call__(self, sentence):
        tokens = self._tokenize(sentence)

        modified_tokens = self._transform_tokens(tokens)

        return self._detokenize(modified_tokens)

    @staticmethod
    def _transform_tokens(tokens):

        modified = []
        for token in tokens:

            append_dot = False
            token_modified = token

            # Handle case when a number is at the end of a sentence.
            if token_modified[-1] == '.':
                token_modified = token_modified[:-1]
                append_dot = True

            # Handle US format like 123.123,50
            if all(char in token for char in ['.', ',']):
                token_modified = token.replace('.', '').replace(',', '.')

            try:
                number = float(token_modified)
                token_modified = num2words(number)

                # TODO: It would be nice to uppercase
                #    the token if it's the first word in a sentence.
                #    Not so easy.

            except ValueError:
                pass

            modified.append(token_modified)

            if append_dot:
                modified.append('.')

        return modified

    @staticmethod
    def _tokenize(sentence):
        """Split text into tokens including punctuation
        and special characters.

        :param sentence: A sentences as a single string.

        :return: List of tokens.
        """
        return re.findall(r"[\w\'-.,]+|[^\s\w]", sentence)


