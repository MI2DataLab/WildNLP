import csv
import filecmp
import os

import custom_tempfile as tempfile
from wildnlp.datasets import IMDB


def get_dataset_obj():
    return IMDB()


def get_path(child_dir=None):
    directory = os.path.join(os.path.dirname(__file__), 'data')

    if child_dir:
        return os.path.join(directory, child_dir)

    return directory


def test_load_single_file():
    file_path = get_path(os.path.join('imdb_sample', 'neg', '0_2.txt'))
    dataset = get_dataset_obj()
    dataset.load(file_path)

    assert len(dataset.data) == 1
    assert 'content' in dataset.data[0]
    assert dataset.data[0]['path'] == '0_2.txt'


def test_load_single_dir():
    path = get_path(os.path.join('imdb_sample', 'neg'))
    dataset = get_dataset_obj()
    dataset.load(path)

    assert len(dataset.data) == 3
    assert 'content' in dataset.data[0]
    assert dataset.data[0]['path'] == os.path.join('neg', '0_2.txt')


def test_load_multiple_dirs():
    path_neg = get_path(os.path.join('imdb_sample', 'neg'))
    path_pos = get_path(os.path.join('imdb_sample', 'pos'))

    dataset = get_dataset_obj()
    dataset.load([path_neg, path_pos])

    assert len(dataset.data) == 6
    assert dataset.data[0]['path'] == os.path.join('neg', '0_2.txt')
    assert dataset.data[-1]['path'] == os.path.join('pos', '2_7.txt')


def test_save_single_file():
    file_path = get_path(os.path.join('imdb_sample', 'neg', '0_2.txt'))
    dataset = get_dataset_obj()
    dataset.load(file_path)

    with tempfile.TemporaryDirectory() as dirname:
        dataset.save(dataset.data, dirname)

        assert filecmp.cmp(file_path, os.path.join(dirname, '0_2.txt'), shallow=False)


def test_save_single_dir():
    path = get_path(os.path.join('imdb_sample', 'neg'))
    dataset = get_dataset_obj()
    dataset.load(path)

    with tempfile.TemporaryDirectory() as dirname:
        dataset.save(dataset.data, dirname)
        for original_file, processed_file \
            in zip(sorted(os.listdir(path)),
                   sorted(os.listdir(os.path.join(dirname, 'neg')))):

            assert filecmp.cmp(os.path.join(path, original_file),
                               os.path.join(dirname, 'neg', processed_file),
                               shallow=False)


def test_save_tsv():
    path = get_path(os.path.join('imdb_sample', 'neg'))
    dataset = get_dataset_obj()
    dataset.load(path)

    with tempfile.TemporaryDirectory() as dirname:
        dataset.save_tsv(dataset.data, os.path.join(dirname, 'test'))

        rows = []
        with open(os.path.join(dirname, 'test'), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for row in reader:
                rows.append(row)

        assert rows[0] == ['Sentiment', 'Content']
        assert rows[1][0] == 'neg'
