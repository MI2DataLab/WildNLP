from wildnlp.aspects import LowerCase


def test_single_word():
    assert LowerCase()("Language") == "language"


def test_sentence():
    sentence = "EU rejects German call to boycott British lamb."
    transformed = LowerCase()(sentence)

    assert transformed == "eu rejects german call to boycott british lamb."
