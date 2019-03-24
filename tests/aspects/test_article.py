from wildnlp.aspects import ArticleSwapper


def test_basic():
    sentence = 'This is a test.'
    modified = ArticleSwapper(swap_probability=1, seed=42)(sentence)

    assert modified == 'This is an test.'


def test_advanced():
    sentence = 'Warsaw was believed to be one of '\
               'the most beautiful cities in the world.'
    modified = ArticleSwapper(swap_probability=1, seed=42)(sentence)

    assert modified == 'Warsaw was believed to be one of '\
                       'a most beautiful cities in a world.'


def test_multiple_sentences():
    sentences = 'This is a dollar sign - $. '\
                'A rabbit, the cute one, is looking for a carrot.'
    modified = ArticleSwapper(swap_probability=1, seed=42)(sentences)

    assert modified == 'This is an dollar sign - $. ' \
                       'A rabbit, a cute one, is looking for carrot.'
