import functools


def compose(*functions):
    """Chains multiple aspects into a single function.

    :param functions: an arbitrary object(s) of the Callable instance.

    :return: chained function
    """
    return functools.reduce(lambda f, g: lambda x: g(f(x)),
                            functions, lambda x: x)
