from wildnlp.aspects import WhiteSpaces


def test_basic():
    sentence = 'Test sentence.'
    modified = WhiteSpaces(add_percentage=100, remove_percentage=0)(sentence)
    print(modified)
    #assert len(modified) == len(word) - 1

    sentence = 'Test sentence.'
    modified = WhiteSpaces(add_percentage=0, remove_percentage=100)(sentence)
    print(modified)
    #assert ...


    #sentence = 'This is a test'
    #modified = RemoveChar(char=' ', words_percentage=100)(sentence)
    #assert len(modified.split()) == 1


