from abc import ABC
from functools import wraps


def file_exists_check(func):

    @wraps(func)
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("Check if the file path is correct")

    return func_wrapper


class Dataset(ABC):

    def __init__(self, *args, **kwargs):
        self._data = []

    @property
    def data(self):
        """Property of the Dataset class.

        :return: Internal object storing a loaded dataset.
        """
        return self._data

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

    def save(self, *args, **kwargs):
        """The method should iterate through texts
        in the dataset and apply a given aspect to them.
        """
        pass
