import numpy as np

from .base import Dataset, file_exists_check


class CoNLL(Dataset):
    """The CoNLL-2003 shared task data for language-independent named
    entity recognition. For details see:
    https://www.clips.uantwerpen.be/conll2003/ner/
    """
    def __init__(self):
        self._dataset_file_header: str = ''
        super().__init__()

    @file_exists_check
    def load(self, path):
        """Reads a CoNLL dataset file
        and loads into internal data structure in the following form:

        ::

            [{tokens: array(<tokens>)
              pos_tags: array(<pos_tags>),
              chunk_tags: array(<chunk_tags>),
              ner_tags: array(<ner_tags>},

              ...,

              ]

        :param path: A path to a file with CoNLL data

        :return: None

        """
        with open(path, "r") as f:
            for line in f.readlines():
                if str(line).startswith('-DOCSTART-'):
                    self._dataset_file_header = str(line)
                    continue

                elif line == "\n":
                    try:
                        processed = self._process_sample(sample)
                        self._data.append(processed)
                    except NameError:
                        pass
                    sample = ""

                else:
                    sample += line

            if sample != "":
                processed = self._process_sample(sample)
                self._data.append(processed)

    def apply(self, aspect, apply_to_ne=False):
        """

        :param aspect: transformation function

        :param apply_to_ne: if `False`, transformation won't be applied
                            to Named Entities. If `True`, transformation
                            will be applied only to Named Entities.

        :return: modified dataset in the following form:

        ::

            [{tokens: array(<tokens>)
              pos_tags: array(<pos_tags>),
              chunk_tags: array(<chunk_tags>),
              ner_tags: array(<ner_tags>},

              ...,

              ]

        """

        modified = []
        for entry in self._data:
            tags = entry['ner_tags']

            if apply_to_ne is False:
                non_ner = np.where(tags == 'O')[0]
            else:
                non_ner = np.where(tags != 'O')[0]

            if len(non_ner) == 0:
                modified.append(entry)
            else:
                sentence = " ".join(entry['tokens'][non_ner])
                modified_sentence = aspect(sentence)

                for idx, token in zip(non_ner, modified_sentence.split()):
                    entry['tokens'][idx] = token

                modified.append(entry)

        return modified

    def save(self, data, path):
        """Saves data in the CoNLL format

        :param data: list of dictionaries in the following form:

        ::

            [{tokens: array(<tokens>)
              pos_tags: array(<pos_tags>),
              chunk_tags: array(<chunk_tags>),
              ner_tags: array(<ner_tags>},

              ...,

              ]

        :param path: Path to save the file. If the file exists,
                     it will be overwritten.

        :return: None
        """

        with open(path, 'w+') as f:

            lines = list()
            lines.append(self._dataset_file_header)

            try:
                for entry in data:
                    line = ""
                    for token, pos_tag, chunk_tag, ner_tag \
                        in zip(entry['tokens'], entry['pos_tags'],
                               entry['chunk_tags'], entry['ner_tags']):
                        line += " ".join([token, pos_tag, chunk_tag, ner_tag]) + '\n'
                    lines.append(line)

                # Remove a trailing newline
                lines[-1] = lines[-1][:-1]
                f.write('\n'.join(lines))
            except KeyError:
                print("The data you're trying to save is corrupted or "
                      "isn't formatted correctly.")

    @staticmethod
    def _process_sample(sample):

        data = sample.split('\n')

        tokens = []
        pos_tags = []
        chunk_tags = []
        ner_tags = []

        for entry in data:
            if entry == '':
                continue

            info = entry.split()
            tokens.append(info[0])
            pos_tags.append(info[1])
            chunk_tags.append(info[2])
            ner_tags.append(info[3])

        processed = dict()
        processed['tokens'] = np.asarray(tokens)
        processed['pos_tags'] = np.asarray(pos_tags)
        processed['chunk_tags'] = np.asarray(chunk_tags)
        processed['ner_tags'] = np.asarray(ner_tags)

        return processed
