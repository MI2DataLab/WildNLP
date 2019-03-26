from wildnlp.aspects import RemoveChar


def test_basic():
    word = 'Test'
    modified = RemoveChar(transform_percentage=100)(word)
    assert len(modified) == len(word) - 1

    sentence = 'This is a test'
    modified = RemoveChar(char=' ', transform_percentage=100)(sentence)
    assert len(modified.split()) == 1

    modified = RemoveChar(char='g', transform_percentage=100)(sentence)
    assert modified == sentence


def test_severity():
    sentence = 'This is a test'
    severity_increases = True
    for percentage in range(25, 101, 25):
        modified = RemoveChar(transform_percentage=percentage)(sentence)
        severity_increases =\
            severity_increases and len(modified) < len(sentence)
        sentence = modified

    assert severity_increases


def test_special_characters():

    assert RemoveChar(transform_percentage=100)('.') == '.'
    assert RemoveChar(transform_percentage=100)('Test!')[-1] == '!'


