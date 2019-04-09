from wildnlp.aspects import AddSubString


def test_basic():

    modified = AddSubString(add_percentage=100)('')
    print(modified)
    assert modified.lower() in ""

    sentence = 'Test sentence.'
    modified = AddSubString(add_percentage=100)(sentence)
    print(modified)
    assert modified[-1] == '.'
    assert len(modified) > len(sentence)
