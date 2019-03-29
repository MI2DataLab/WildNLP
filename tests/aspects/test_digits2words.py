from wildnlp.aspects import Digits2Words


def test_basic():
    sentence = '22'
    modified = Digits2Words()(sentence)

    assert modified == 'twenty-two'

    sentence = 'That\'s 23.3.'
    modified = Digits2Words()(sentence)

    assert modified == 'That\'s twenty-three point three.'

    sentence = 'Famous 12. 2 to midnight.'
    modified = Digits2Words()(sentence)

    assert modified == 'Famous twelve. two to midnight.'
