from abc import ABC


class Dataset(ABC):

    def load(self, *args, **kwargs):
        """The method should handle loading
        and parsing of a specific dataset.
        """
        pass

    def apply(self, *args, **kwargs):
        """The method should iterate through texts
        in the dataset and apply a given aspect to them.
        """
        pass
