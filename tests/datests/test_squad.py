import filecmp
import os
import tempfile

from wildnlp.datasets import SQuAD
from wildnlp.aspects.dummy import Reverser
from wildnlp.aspects.utils import compose


def get_dataset_obj():
    return SQuAD()


def get_file_path(filename):
    directory = os.path.join(os.path.dirname(__file__), 'data')

    return os.path.join(directory, filename)


def test_save_original():
    filename = 'squad_v1_sample.json'
    dataset = get_dataset_obj()
    dataset.load(get_file_path(filename))

    with tempfile.TemporaryDirectory() as dirname:
        test_file_path = os.path.join(dirname, 'test')
        dataset.save(dataset.data, test_file_path)

        assert filecmp.cmp(get_file_path(filename), test_file_path, shallow=False)


def test_save_modified():
    filename = 'squad_v1_sample.json'
    dataset = get_dataset_obj()
    dataset.load(get_file_path(filename))

    # Reversing two times equals to original input
    composed = compose(Reverser(), Reverser())
    modified = dataset.apply(composed)

    with tempfile.TemporaryDirectory() as dirname:
        test_file_path = os.path.join(dirname, 'test')
        dataset.save(modified, test_file_path)

        assert filecmp.cmp(get_file_path(filename), test_file_path, shallow=False)


def test_save_original():
    filename = 'squad_v2_sample.json'
    dataset = get_dataset_obj()
    dataset.load(get_file_path(filename))

    with tempfile.TemporaryDirectory() as dirname:
        test_file_path = os.path.join(dirname, 'test')
        dataset.save(dataset.data, test_file_path)

        assert filecmp.cmp(get_file_path(filename), test_file_path, shallow=False)


def test_save_modified():
    filename = 'squad_v2_sample.json'
    dataset = get_dataset_obj()
    dataset.load(get_file_path(filename))

    # Reversing two times equals to original input
    composed = compose(Reverser(), Reverser())
    modified = dataset.apply(composed)

    with tempfile.TemporaryDirectory() as dirname:
        test_file_path = os.path.join(dirname, 'test')
        dataset.save(modified, test_file_path)

        assert filecmp.cmp(get_file_path(filename), test_file_path, shallow=False)