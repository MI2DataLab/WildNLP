from wildnlp.aspects import PigLatin


def test_single_word():
    assert PigLatin()("Language") == "anguagelay"


def test_sentence():
    sentence = "this is a sample sentence."
    transformed = PigLatin()(sentence)

    assert transformed == "histay siay aay amplesay entence.say"
