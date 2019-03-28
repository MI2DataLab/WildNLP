from wildnlp.aspects import Misspelling


def test_basic():
    sentence = 'aggressive.'
    modified = Misspelling()(sentence)

    assert modified == 'agressive.'

    sentence = 'Aggressive.'
    modified = Misspelling()(sentence)

    assert modified == 'Agressive.'

    sentence = "That's awful"
    modified = Misspelling()(sentence)

    assert len(modified.split()) == 2
    assert modified.split()[-1] in ["awfull", "aweful"]

