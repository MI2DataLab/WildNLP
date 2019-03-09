from .base import Aspect


class Reverser(Aspect):
    """Reverse all characters in words.
    """

    def __call__(self, sentence):
        return " ".join([self._transform_word(word)
                        for word in sentence.split()])

    @staticmethod
    def _transform_word(word):
        if len(word) == 0:
            raise ValueError("Can't transfer empty strings!")
        return word[::-1]
