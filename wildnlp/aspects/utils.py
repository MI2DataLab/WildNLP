import functools


def compose(*functions):
    """Chains multiple aspects into a single function.

    :param functions: Object(s) of the Callable instance.

    :return: chained function

    Example::

        from wildnlp.aspects.utils import compose
        from wildnlp.aspects import Swap, QWERTY

        composed_aspect = compose(Swap(), QWERTY())
        modified_text = composed_aspect('Text to corrupt')

    """
    return functools.reduce(lambda f, g: lambda x: g(f(x)),
                            functions, lambda x: x)
