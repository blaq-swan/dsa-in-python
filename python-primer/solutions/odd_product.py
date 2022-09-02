#!/usr/bin/python3
"""finds pairs of odd"""


def odd_products(sequence):
    """checks if two numbers have odd product
    Args:
        sequence: a sequence of integers
    Returns:
        a list of pairs of numbers whose product is odd
    """

    if not isinstance(sequence, (list, tuple, range)):
        raise TypeError("argument must be a sequence")
    for num in sequence:
        if not isinstance(num, int):
            raise TypeError("input must be a sequence of integers")

    output = []
    for x in range(len(sequence)):
        for y in range(x + 1, len(sequence)):
            if (sequence[x] * sequence[y]) & 1 == 1:
                output += [(sequence[x], sequence[y])]

    return output
