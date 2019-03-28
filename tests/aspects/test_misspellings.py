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


def test_homophones():
    sentence = 'bald'
    modified = Misspelling(use_homophones=True)(sentence)

    assert modified in ["balled", "bawled"]

    sentence = 'Bald'
    modified = Misspelling(use_homophones=True)(sentence)

    assert modified in ["Balled", "Bawled"]

    sentence = 'we\'ll'
    modified = Misspelling(use_homophones=True)(sentence)

    assert modified in ["weal", "wheal", "wheel"]

