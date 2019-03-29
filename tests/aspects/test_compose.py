from wildnlp.aspects.utils import compose
from wildnlp.aspects.dummy import PigLatin, Reverser


def test_single_word_piglatin_first():
    composed = compose(PigLatin(), Reverser())

    assert composed("Language") == "yalegaugna"


def test_single_word_reverser_first():
    composed = compose(Reverser(), PigLatin())
    assert composed("Language") == "gaugnaleay"


def test_single_word_reverser_first_combined():
    composed = compose(Reverser(), PigLatin(), Reverser())
    assert composed("Language") == "yaelanguag"

