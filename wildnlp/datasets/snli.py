import json

from .base import Dataset, file_exists_check


class SNLI(Dataset):
    """The SNLI dataset supporting the task of natural language inference.
    For details see: https://nlp.stanford.edu/projects/snli/
    """

    @file_exists_check
    def load(self, path):
        """Loads a SNLI dataset.

        :param path: A path to a SNLI data file in JSONL format.

        :return: None
        """
        with open(path, 'r') as f:
            for line in f.readlines():
                self._data.append(json.loads(line))

    def apply(self, aspect):
        """Modifies premises (sentence1) in the dataset
        leaving other data intact.
        """

        # TODO: modify parsed sentences as well.

        modified = []
        for entry in self._data:
            try:

                modified_sentence = aspect(entry['sentence1'])
                entry['sentence1'] = modified_sentence
                modified.append(entry)

            except KeyError:
                print("Encountered a KeyError. The entry won't be modified")
                modified.append(entry)

        return modified

    def save(self, data, path):
        """Saves data in the SNLI format
        """
        json_strings = [json.dumps(entry) for entry in data]

        with open(path, 'w') as f:
            f.write("\n".join(json_strings))
