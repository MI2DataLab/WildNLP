from ..base import Aspect


class PigLatin(Aspect):
    """See wikipedia https://en.wikipedia.org/wiki/Pig_Latin
    """

    def __call__(self, sentence):
        return " ".join([self._transform_word(word)
                        for word in sentence.split()])

    @staticmethod
    def _transform_word(word):
        if len(word) == 0:
            raise ValueError("Can't transfer empty strings!")
        transformed_word = word[1:] + word[0] + 'ay'
        return transformed_word.lower()
