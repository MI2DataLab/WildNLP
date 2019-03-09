from abc import ABC


class Aspect(ABC):
    """Base, abstract class. All the aspects
    must implement the __call__ method.
    """

    def __call__(self, sentence, *args, **kwargs):
        """We want to directly call
        objects of the Aspect class for easy chaining.
        This function will be applied to sentences.
        """
        pass
