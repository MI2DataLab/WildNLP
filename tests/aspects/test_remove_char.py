from wildnlp.aspects import RemoveChar


def test_basic():
    word = 'Test'
    modified = RemoveChar(words_percentage=100)(word)
    assert len(modified) == len(word) - 1

    word = 'Test'
    modified = RemoveChar(words_percentage=100,
                          characters_percentage=0)(word)
    assert word == modified

    word = 'Test'
    modified = RemoveChar(words_percentage=0,
                          characters_percentage=100)(word)
    assert word == modified

    sentence = 'This is a test'
    modified = RemoveChar(char=' ', words_percentage=100)(sentence)
    assert len(modified.split()) == 1

    modified = RemoveChar(char='g', words_percentage=100)(sentence)
    assert modified == sentence


def test_severity():
    sentence = 'This is a test'
    severity_increases = True
    for percentage in range(25, 101, 25):
        modified = RemoveChar(words_percentage=percentage,
                              characters_percentage=50)(sentence)
        severity_increases =\
            severity_increases and len(modified) < len(sentence)
        sentence = modified

    assert severity_increases


def test_special_characters():

    assert RemoveChar(words_percentage=100)('.') == '.'
    assert RemoveChar(words_percentage=100)('Test!')[-1] == '!'
