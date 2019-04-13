from wildnlp.aspects import QWERTY


def test_basic():

    for i in range(10):
        modified = QWERTY(words_percentage=100)('T')
        assert modified.isupper() or modified.isdigit()
        assert modified.lower() in 'r56yhgf'


def test_severity():
    sentence = 'warsaw was believed to be the most beautiful.'
    modified = QWERTY(words_percentage=100, seed=42)(sentence)
    assert all(token not in modified.split() for token in sentence.split())

    modified = QWERTY(words_percentage=50, seed=42)(sentence)
    assert any(token in modified.split() for token in sentence.split())

    modified = QWERTY(words_percentage=0, seed=42)(sentence)
    assert all(token in modified.split() for token in sentence.split())


def test_advanced():
    sentence = 'Warsaw was believed to be one of '\
               'the most beautiful cities in the world.'
    modified = QWERTY(words_percentage=100, seed=42)(sentence)

    assert modified[-1] == '.'
    assert len(modified.split()) == len(sentence.split())


def test_multiple_sentences():
    sentences = 'This is a dollar sign - $. '\
                'A rabbit, the cute one, is looking for a carrot.'
    modified = QWERTY(words_percentage=100, seed=42)(sentences)

    assert modified[-1] == '.'
    assert len(modified.split()) == len(sentences.split())
