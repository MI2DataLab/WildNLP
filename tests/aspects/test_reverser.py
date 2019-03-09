from wildnlp.aspects import Reverser


def test_single_word():
    assert Reverser()("Language") == "egaugnaL"


def test_sentence():
    sentence = "this is a sample sentence."
    transformed = Reverser()(sentence)

    assert transformed == "siht si a elpmas .ecnetnes"
