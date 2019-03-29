import random

from .base import Aspect


class Articles(Aspect):
    """Randomly removes or swaps articles into wrong ones.

    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, swap_probability=0.5, seed=42):
        """

        :param swap_probability: Probability of applying a transformation.
                                 Defaults to 0.5.

        :param seed: Random seed.
        """

        self._articles = ['a', 'an', 'the', '']
        self._swap_probability = swap_probability
        random.seed(seed)

    def __call__(self, sentence):
        tokens = self._tokenize(sentence)
        swapped_tokens = self._swap_articles(tokens)

        return self._detokenize(swapped_tokens)

    def _swap_articles(self, tokens):

        modified = []
        for token in tokens:
            if token.lower() in self._articles \
               and random.random() < self._swap_probability:

                articles_copy = self._articles.copy()
                articles_copy.remove(token.lower())
                selected_article = random.choice(articles_copy)

                # TODO: Added handling the case when the article being
                #     modified is at the beginning of a sentence.
                if token[0].isupper():
                    selected_article = self._capitalize(selected_article)

                token = selected_article

            modified.append(token)

        return modified

    @staticmethod
    def _capitalize(token):
        try:
            return token[0].upper() + token[1:]
        except IndexError:
            return token


