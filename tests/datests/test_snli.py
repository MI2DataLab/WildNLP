import filecmp
import os
import tempfile

from wildnlp.datasets import SNLI
from wildnlp.aspects.dummy import Reverser
from wildnlp.aspects.utils import compose


def get_dataset_obj():
    return SNLI()


def get_file_path():
    directory = os.path.join(os.path.dirname(__file__), 'data')
    filename = 'snli_sample.jsonl'

    return os.path.join(directory, filename)


def test_load():
    dataset = SNLI()
    dataset.load(get_file_path())

    assert len(dataset.data) == 3
    assert sorted(dataset.data[0].keys()) == \
        ['annotator_labels', 'captionID', 'gold_label', 'pairID',
         'sentence1', 'sentence1_binary_parse', 'sentence1_parse',
         'sentence2', 'sentence2_binary_parse', 'sentence2_parse']


def test_modify():
    dataset = SNLI()
    dataset.load(get_file_path())

    modified = dataset.apply(Reverser())

    assert modified[2]['sentence1'] == 'sihT hcruhc riohc sgnis ot eht sessam sa yeht '\
                                       'gnis suoyoj sgnos morf eht koob ta a .hcruhc'
    assert len(modified) == 3
    assert sorted(modified[0].keys()) == \
           ['annotator_labels', 'captionID', 'gold_label', 'pairID',
            'sentence1', 'sentence1_binary_parse', 'sentence1_parse',
            'sentence2', 'sentence2_binary_parse', 'sentence2_parse']


def test_save_original():

    dataset = get_dataset_obj()
    dataset.load(get_file_path())

    with tempfile.TemporaryDirectory() as dirname:
        test_file_path = os.path.join(dirname, 'test')
        dataset.save(dataset.data, test_file_path)

        assert filecmp.cmp(get_file_path(), test_file_path, shallow=False)


def test_save_modified():

    dataset = get_dataset_obj()
    dataset.load(get_file_path())

    # Reversing two times equals to original input
    composed = compose(Reverser(), Reverser())
    modified = dataset.apply(composed)

    with tempfile.TemporaryDirectory() as dirname:
        test_file_path = os.path.join(dirname, 'test')
        dataset.save(modified, test_file_path)

        assert filecmp.cmp(get_file_path(), test_file_path, shallow=False)
