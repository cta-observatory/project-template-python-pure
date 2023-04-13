"""
Template pure python projects.
"""
from .version import __version__

__all__ = [
    "__version__",
    "fibonacci",
]


def fibonacci(n):
    """
    Calculate the nth fibonacci number.

    Parameters
    ----------
    n : `int`
       Which number to calculate, n >= 0.

    Returns
    -------
    fib_n : `int`
        The nth fibonacci number

    Examples
    --------
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    """

    if n < 0:
        raise ValueError(f"n must be >= 0, got {n}")

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
