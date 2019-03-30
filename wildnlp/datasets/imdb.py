import csv
from io import open
import os

from .base import Dataset


class IMDB(Dataset):
    """The IMDB dataset containing movie reviews for a sentiment analysis.
    The dataset consists of 50 000 reviews of two classes, negative and positive.
    Each review is stored in a separate text file.
    For details see: http://ai.stanford.edu/~amaas/data/sentiment/
    """

    def load(self, path):
        """Loads a SNLI dataset.

        :param path: A path to single file, directory containing review files
                     or list of paths to such directories.

        :return: None
        """

        if type(path) is str and os.path.isdir(path):
            self._load_multiple_files(path)

        elif type(path) is list:
            for single_path in path:
                self._load_multiple_files(single_path)

        elif os.path.isfile(path):
            _, filename = os.path.split(path)
            entry = {'path': filename,
                     'content': self._read_file(path)}
            self._data.append(entry)

    def apply(self, aspect):
        """Modifies contents of the whole files in the IMDB dataset.
        """

        modified = []
        for entry in self._data:
            modified_sentence = aspect(entry['content'])
            entry['content'] = modified_sentence
            modified.append(entry)

        return modified

    def save(self, data, path):
        """Saves IMDB reviews to separate files
        with the original names.

        :param path: path to a top directory where files will be saved.

        :return: None
        """

        for entry in data:
            directory, filename = os.path.split(entry['path'])
            full_path = os.path.join(path, directory)
            if not os.path.exists(full_path) and directory != '':
                os.makedirs(full_path)
            with open(os.path.join(path, entry['path']), 'w') as f:
                f.write(entry['content'])

    def save_tsv(self, data, path):
        """Convenience function for saving IMDB reviews into a single TSV file.

        :param path: Path to a tab separated file.

        :return: None
        """

        with open(path, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow(['Sentiment', 'Content'])

            for entry in data:
                directory, _ = os.path.split(entry['path'])
                if directory == 'neg':
                    sentiment = 'neg'
                elif directory == 'pos':
                    sentiment = 'pos'
                else:
                    sentiment = 'unsup'

                writer.writerow([sentiment, entry['content']])

    @staticmethod
    def _read_file(path):

        with open(path, 'r') as f:
            content = f.read()

        return content

    def _load_multiple_files(self, path):

        filenames = os.listdir(path)
        for filename in filenames:
            full_path = os.path.join(path, filename)

            _, patent_dir = os.path.split(path)
            entry = {'path': os.path.join(patent_dir, filename),
                     'content': self._read_file(full_path)}
            self._data.append(entry)
