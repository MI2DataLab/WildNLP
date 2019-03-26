from wildnlp.aspects import Articles


def test_basic():
    sentence = 'This is a test.'
    modified = Articles(swap_probability=1, seed=42)(sentence)

    assert modified.split()[0] == 'This'
    assert modified.split()[2] != 'a'


def test_advanced():
    sentence = 'Warsaw was believed to be one of '\
               'the most beautiful cities in the world.'
    modified = Articles(swap_probability=1, seed=42)(sentence)

    assert 'the' not in modified.split()


def test_multiple_sentences():
    sentences = 'This is a dollar sign - $. '\
                'A rabbit, the cute one, is looking for a carrot.'
    modified = Articles(swap_probability=1, seed=42)(sentences)

    assert len(modified.split('.')) == 3
    assert modified.split('.')[-1] == ''

    second_sentence = modified.split('.')[1]
    assert second_sentence[0] == ' '
    assert second_sentence[1].isupper() or second_sentence[1] == ''
