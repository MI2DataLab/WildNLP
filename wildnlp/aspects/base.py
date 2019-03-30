from abc import ABC
import re


class Aspect(ABC):
    """Base, abstract class. All the aspects
    must implement the __call__ method.
    """

    def __call__(self, sentence):
        """We want to directly call
        objects of the Aspect class for easy chaining.
        This function will be applied to sentences.
        """
        pass

    @staticmethod
    def _tokenize(sentence):
        """Split text into tokens including punctuation
        and special characters.

        :param sentence: A sentences as a single string.

        :return: List of tokens.
        """
        return re.findall(r"[\w\'\-()*]+|[^\s\w]", sentence)

    @staticmethod
    def _detokenize(tokens):
        """Join tokens into tokens including punctuation
        and special characters.

        :param tokens: List of tokens.

        :return: A sentence as a single string.
        """

        sentence = " ".join(tokens)

        # remove space between words and punctuation
        sentence = re.sub(r'\s([?.!,:;\'\"\\](?:\s|$))', r'\1', sentence)

        # remove double spaces
        return " ".join(sentence.split())


