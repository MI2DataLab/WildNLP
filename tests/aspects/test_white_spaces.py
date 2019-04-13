from wildnlp.aspects import WhiteSpaces


def test_basic():
    sentence = 'Test sentence.'
    modified = WhiteSpaces(white_spaces=" \t", add_percentage=100, remove_percentage=0, seed=40)(sentence)
    print(modified)
    assert len(modified) > len(sentence)

    sentence = 'Test sentence.'
    modified = WhiteSpaces(white_spaces=" \t", add_percentage=0, remove_percentage=100)(sentence)
    print(modified)

    assert modified[-1] == '.'
    assert len(modified.split()) < len(sentence.split())

    sentence = 'Test'
    modified = WhiteSpaces(white_spaces=" ", add_percentage=0, remove_percentage=0)(sentence)
    print(modified)

    assert modified == sentence

    sentence = 'Test'
    modified = WhiteSpaces(white_spaces=" ", add_percentage=0, remove_percentage=100)(sentence)
    print(modified)

    assert modified == sentence

    sentence = 'Test sent'
    white_spaces=" "
    modified = WhiteSpaces(white_spaces=white_spaces, add_percentage=100, remove_percentage=0)(sentence)
    print(modified)

    assert len(modified) > len(sentence)
    assert modified[-1] in white_spaces + sentence[-1]
