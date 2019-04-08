from wildnlp.aspects import AddSubString


def test_basic():

    for i in range(10):
        modified = AddSubString(add_percentage=100)('')
        print(modified)
        #assert modified.isupper() or modified.isdigit()
        assert modified.lower() in ""

