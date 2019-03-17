from .base import Dataset


class SampleDataset(Dataset):
    """Simple list of sentences solely
    for testing and example purpose.
    """

    def __init__(self):
        self._data = None

    def load(self):
        self._data = [
            "Manning is a leader in applying Deep Learning "
            "to Natural Language Processing",
            "Manning has coauthored leading textbooks on statistical "
            "approaches to Natural Language Processing"
        ]

    def apply(self, aspect):
        return [aspect(sentence) for sentence in self._data]

    def save(self):
        pass
