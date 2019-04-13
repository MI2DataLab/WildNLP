from wildnlp.aspects import ChangeChar


def test_basic():

    for i in range(4):
        modified = ChangeChar(words_percentage=100,seed=i)('l')

        assert modified in 'I1|i'


def test_severity():
    sentence = 'warsaw was believed to be the most beautiful. Jest piękną stolicą, ń, ś, ćma.'
    modified = ChangeChar(words_percentage=100, seed=42)(sentence)

    assert any(token not in modified.split() for token in sentence.split())

    modified = ChangeChar(words_percentage=50, seed=42)(sentence)

    assert any(token in modified.split() for token in sentence.split())

    modified = ChangeChar(words_percentage=0, seed=42)(sentence)

    assert all(token in modified.split() for token in sentence.split())


def test_advanced():
    sentence = 'Warsaw was believed to be one of '\
               'the most beautiful cities in the world.'
    modified = ChangeChar(words_percentage=100, seed=42)(sentence)

    assert modified[-1] == '.'
    assert len(modified.split()) == len(sentence.split())


def test_multiple_sentences():
    sentences = 'This is a dollar sign - $. '\
                'A rabbit, the cute one, is looking for a carrot.'
    modified = ChangeChar(words_percentage=100, seed=42)(sentences)

    assert modified[-1] == '.'
    assert len(modified.split()) == len(sentences.split())
