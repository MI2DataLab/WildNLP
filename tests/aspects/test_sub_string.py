from wildnlp.aspects import AddSubString


def test_basic():

    modified = AddSubString(add_percentage=100)('')

    assert modified.lower() in ""

    sentence = 'Test sentence.'
    modified = AddSubString(add_percentage=100)(sentence)

    assert modified[-1] == '.'
    assert len(modified) > len(sentence)
