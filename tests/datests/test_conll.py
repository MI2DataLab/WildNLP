import filecmp
import os
import tempfile

from wildnlp.datasets import CoNLL
from wildnlp.aspects.dummy import Reverser
from wildnlp.aspects.utils import compose


def get_file_path():
    directory = os.path.join(os.path.dirname(__file__), 'data')
    filename = 'conll2003_sample.txt'

    return os.path.join(directory, filename)


def test_load():
    dataset = CoNLL()
    dataset.load(get_file_path())

    assert len(dataset.data) == 3
    assert dataset.data[0]['tokens'][0] == 'EU'
    assert dataset.data[2]['pos_tags'][0] == 'NNP'
    assert len(dataset.data[2]['tokens']) == 2


def test_modify_mask_ne():
    dataset = CoNLL()
    dataset.load(get_file_path())

    modified = dataset.apply(Reverser(), apply_to_ne=False)

    assert modified[0]['tokens'][0] == 'EU'
    assert modified[0]['tokens'][1] == 'stcejer'
    assert modified[1]['tokens'][0] == 'Peter'


def test_modify_mask_non_ne():
    dataset = CoNLL()
    dataset.load(get_file_path())

    modified = dataset.apply(Reverser(), apply_to_ne=True)

    assert modified[0]['tokens'][0] == 'UE'
    assert modified[0]['tokens'][1] == 'rejects'
    assert modified[1]['tokens'][0] == 'reteP'


def test_save_original():

    dataset = CoNLL()
    dataset.load(get_file_path())

    with tempfile.TemporaryDirectory() as dirname:
        test_file_path = os.path.join(dirname, 'test.txt')
        dataset.save(dataset.data, test_file_path)

        assert filecmp.cmp(get_file_path(), test_file_path, shallow=False)


def test_save_modified():

    dataset = CoNLL()
    dataset.load(get_file_path())

    # Reversing two times equals to original input
    composed = compose(Reverser(), Reverser())
    modified = dataset.apply(composed)

    with tempfile.TemporaryDirectory() as dirname:
        test_file_path = os.path.join(dirname, 'test.txt')
        dataset.save(modified, test_file_path)

        assert filecmp.cmp(get_file_path(), test_file_path, shallow=False)
