from wildnlp.aspects import ChangeChar


def test_basic():

    for i in range(10):
        modified = ChangeChar(words_percentage=100)('L')
        print(modified)
        assert modified.isupper() or modified.isdigit()
        assert modified in 'I|1'



