from wildnlp.aspects import Punctuation


def test_basic():
    sentence = 'Great'
    modified = Punctuation(add_percentage=0, remove_percentage=100)(sentence)

    assert modified == sentence

    sentence = 'Great,'
    modified = Punctuation(char=',', add_percentage=0,
                           remove_percentage=100)(sentence)

    assert modified == 'Great'

    sentence = 'Great,'
    modified = Punctuation(char=',', add_percentage=100,
                           remove_percentage=0)(sentence)

    assert modified[-2:] != ',,'

    sentence = 'This is the end.'
    modified = Punctuation(char=',', add_percentage=100,
                           remove_percentage=100)(sentence)

    assert modified == 'This, is, the, end.'
