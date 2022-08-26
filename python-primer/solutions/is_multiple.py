#!/usr/bin/python3
"""1_is-multiple"""


def is_multiple(n, m) -> bool:
    """Checks if n is a multiple of m
    Args:
        n: number
        m: multiple
    Returns:
        True if n is a multiple of n, False otherwise
    """

    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if not isinstance(m, int):
        raise TypeError('m must be an integer')

    return True if n % m == 0 else False
