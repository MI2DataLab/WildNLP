from wildnlp.aspects import SentimentMasking


def test_negative():
    sentence = '2-faced'
    modified = SentimentMasking()(sentence)

    assert modified != sentence

    sentence = 'adaptable'
    modified = SentimentMasking()(sentence)

    assert modified == sentence


def test_positive():
    sentence = '2-faced'
    modified = SentimentMasking(use_positive=True)(sentence)

    assert modified == sentence

    sentence = 'adaptable'
    modified = SentimentMasking(use_positive=True)(sentence)

    assert modified != sentence

