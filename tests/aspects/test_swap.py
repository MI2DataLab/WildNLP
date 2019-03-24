from wildnlp.aspects import CharacterSwapper


def test_basic():
    sentence = 'This is a test.'
    modified = CharacterSwapper(num_words_to_swap=1, seed=42)(sentence)
    modified_2 = CharacterSwapper(num_words_to_swap=2, seed=42)(sentence)
    modified_10 = CharacterSwapper(num_words_to_swap=10, seed=42)(sentence)

    assert modified == 'This is a tset.'
    assert modified_2 == 'Tihs is a tets.'
    assert modified_10 == 'Tihs is a tets.'


def test_advanced():
    sentence = 'Warsaw was believed to be one of '\
               'the most beautiful cities in the world.'
    modified = CharacterSwapper(num_words_to_swap=5, seed=42)(sentence)

    assert modified == 'Warsaw was belieevd to be oen of '\
                       'the msot beautiful ctiies in teh world.'


def test_multiple_sentences():
    sentences = 'This is a dollar sign - $. '\
                'A rabbit, the cute one, is looking for a carrot.'
    modified = CharacterSwapper(num_words_to_swap=5, seed=42)(sentences)

    modified == 'This is a dollar sing - $. '\
                'A rbabit, the ctue one, is looking fro a carrot.'
