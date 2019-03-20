import json

from .base import Dataset, file_exists_check


class SQuAD(Dataset):
    """The SQuAD dataset
    For details see: https://rajpurkar.github.io/SQuAD-explorer/
    """

    def __init__(self):
        self._data = None

    @file_exists_check
    def load(self, path):
        """Loads a SQuAD dataset.

        :param path: A path to a SQuAD data file in JSONL format.

        :return: None
        """
        with open(path, 'r') as f:
            self._data = json.load(f)

    def apply(self, aspect):
        """Modifies questions in the dataset
        leaving other data intact.
        """

        modified = self._data.copy()
        for entry in modified['data']:

            for paragraph in entry['paragraphs']:
                for qa in paragraph['qas']:
                    modified_sentence = aspect(qa['question'])
                    qa['question'] = modified_sentence

        return modified

    def save(self, data, path):
        """Saves data in the SQuAD format
        """

        with open(path, 'w') as f:
            json.dump(data, f)

