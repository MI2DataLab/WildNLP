from .base import Aspect


class LowerCase(Aspect):
    """Lower-cases the dataset

    """

    def __call__(self, sentence):
        return " ".join([self._lowercase_word(word)
                         if word != '' else ''
                         for word in sentence.split(' ')])

    @staticmethod
    def _lowercase_word(word):
        if len(word) == 0:
            raise ValueError("Can't lowercase empty words")
        return word.lower()
