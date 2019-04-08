"""
Minimal test of all classes inheriting from the Aspect class.

Part of the test is manual, i.e. a human is expected to visually
asses if there are no apparent problems with a transformed sentence.
"""

import difflib
import inspect

from wildnlp.aspects import *
from wildnlp.aspects.base import Aspect


def test_all():

    sentence = 'We\'re testing almost all of the aspects ' \
               'at once, 11 (or more) with a stupid style.'
    modules = globals().copy()
    for k, v in modules.items():
        if not inspect.isclass(v):
            continue

        if issubclass(v, Aspect) and v is not Aspect:
            transformed = v()(sentence)
            assert isinstance(transformed, str)
            #print("\n{}:\n original: {}\n modified: {}\n diff: {}"
            #      .format(k, sentence, transformed,
            #              color_diff(sentence, transformed)))

            transformed_word = v()('Works')
            assert isinstance(transformed_word, str)


def color_diff(original, modified):
    output = ""
    for char in list(difflib.ndiff(original, modified)):
        if char[0] == ' ':
            output += char[-1]
        elif char[0] == '+':
            output += '\033[92m' + char[-1] + '\033[0m'
        elif char[0] == '-':
            output += '\033[91m' + char[-1] + '\033[0m'

    return output

