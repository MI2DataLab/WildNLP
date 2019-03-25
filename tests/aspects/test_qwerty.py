from wildnlp.aspects import QWERTYSwapper


def test_basic():

    for i in range(10):
        modified = QWERTYSwapper(num_words_to_swap=1)('T')
        assert modified in 'r56yhgf'


def test_advanced():
    sentence = 'Warsaw was believed to be one of '\
               'the most beautiful cities in the world.'
    modified = QWERTYSwapper(num_words_to_swap=5, seed=42)(sentence)

    assert modified[-1] == '.'
    assert len(modified.split()) == len(sentence.split())


def test_multiple_sentences():
    sentences = 'This is a dollar sign - $. '\
                'A rabbit, the cute one, is looking for a carrot.'
    modified = QWERTYSwapper(num_words_to_swap=5, seed=42)(sentences)

    assert modified[-1] == '.'
    assert len(modified.split()) == len(sentences.split())

