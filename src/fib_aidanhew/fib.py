"""
A module that generates Fibonacci numbers.

This module provides a function to generate all Fibonacci numbers
less than a specified integer.
"""


def fib_before_n(n):
    """
    Return all Fibonacci numbers less than a given value.

    This function generates the sequence iteratively and returns
    all Fibonacci numbers that are strictly less than `n`.

    Parameters
    ----------
    n : int
        All returned Fibonacci numbers will be strictly less than 
        this value.

    Returns
    -------
    list of int
        A list containing the Fibonacci numbers less than `n`.

    Raises
    ------
    TypeError
        If `n` is not an integer.
    ValueError
        If `n` is less than or equal to 0.

    Examples
    --------
    >>> fib_before_n(10)
    [0, 1, 1, 2, 3, 5, 8]
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    fibs = [0, 1]
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])

    return [f for f in fibs if f < n]
