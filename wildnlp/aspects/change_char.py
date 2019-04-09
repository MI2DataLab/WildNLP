import json
import os
import random

from .base import Aspect


class ChangeChar(Aspect):
    """Simulates errors made while writing on a QWERTY-type keyboard.
    Characters are swapped with their neighbors on the keyboard.

    .. caution:: Uses random numbers, default seed is 42.
    """

    def __init__(self, mistakes_type="ocr", words_percentage=1, characters_percentage=10,
                 seed=42):
        """

        :param mistakes_type: Type of dictionary of replacement chars:
            qwerty, ocr or other (listed in json file).

        :param words_percentage: Percentage of words in a
            sentence that should be transformed. If greater than 0,
            always at least single word will be transformed.

        :param characters_percentage: Percentage of characters in a
            word that should be transformed. If greater than 0
            always at least single character will be transformed.

        :param seed: Random seed.
        """

        # TODO According to the original implementation
        #     it seem's that the variable should default to 1
        #     (when it was referring to absolute numbers)
        if words_percentage >= 1:
            words_percentage /= 100.

        if characters_percentage >= 1:
            characters_percentage /= 100.

        self._words_percentage = words_percentage
        self._characters_percentage = characters_percentage

        self._mistakes = self._load_mistakes(mistakes_type)

        random.seed(seed)

    def __call__(self, sentence):
        tokens = self._tokenize(sentence)

        modified_tokens = self._transform_tokens(tokens)

        return self._detokenize(modified_tokens)

    def _transform_tokens(self, tokens):

        # TODO Differently to other aspects, here
        #    we don't filter out punctuations etc.
        tokens_idx = list(range(len(tokens)))
        random.shuffle(tokens_idx)

        selected_tokens = \
            sorted(tokens_idx[:self._percentage_to_num(
                tokens, self._words_percentage)])

        modified = []
        for i, token in enumerate(tokens):
            if i in selected_tokens:
                token = self._transform_token(token)
            modified.append(token)

        return modified

    def _transform_token(self, token):

        try:
            selected_chars = [i for i, _ in enumerate(token)]
            random.shuffle(selected_chars)

            selected_chars = \
                sorted(selected_chars[:self._percentage_to_num(
                    token, self._characters_percentage)])

            transformed_token = ""
            for i, char in enumerate(token):
                if i in selected_chars:
                    possible_mistakes = \
                        self._mistakes[char.lower()]
                    mistake = random.choice(possible_mistakes)

                    if char.isupper():
                        char = mistake.upper()
                    else:
                        char = mistake

                transformed_token += char

        except KeyError:
            transformed_token = token

        return transformed_token

    @staticmethod
    def _load_mistakes(mistakes_type):

        # TODO make a common superClass for QWERTY and OCR and ChangeChar (or just change the mistakes_type)

        filename = mistakes_type + ".json"
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, 'auxiliary', filename)
        with open(path, 'r', encoding="UTF-8") as f:
            mistakes = json.load(f)

        return mistakes

    @staticmethod
    def _percentage_to_num(array, percentage):
        # Ensure that at least one item will be transformed.
        if percentage == 0:
            return 0
        return max(1, int(len(array) * percentage))
