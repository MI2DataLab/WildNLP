from wildnlp.aspects import Swap


def test_basic():
    sentence = 'This is a test.'
    modified = Swap(transform_percentage=100, seed=42)(sentence)
    modified_50 = Swap(transform_percentage=25, seed=42)(sentence)

    assert all(token not in modified.split() for token in ['This', 'test.'])
    assert 'This' not in modified_50.split()\
           or 'test.' not in modified_50.split()


def test_advanced():
    sentence = 'Warsaw was believed to be one of '\
               'the most beautiful cities in the world.'
    modified = Swap(transform_percentage=100, seed=42)(sentence)

    assert all(token in modified.split() for token in
               [token for token in sentence.split() if len(token) <= 2])

    assert all(token not in modified.split() for token in
               [token for token in sentence.split() if len(token) > 2])


def test_multiple_sentences():
    sentences = 'This is a dollar sign - $. '\
                'A rabbit, the cute one, is looking for a carrot.'
    modified = Swap(transform_percentage=50, seed=42)(sentences)

    assert modified != sentences
    assert sentences[-1] == '.'
