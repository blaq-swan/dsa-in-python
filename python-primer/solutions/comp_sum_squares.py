#!/usr/bin/python3
"""comp_square_sum module"""


def comp_square_sum(n) -> int:
    """
    finds sum of the squares of all the positive integers smaller than
    Args:
        n: number limit
    Returns:
        sum of all positive integers
    """

    assert int(n) == n and n >= 0, "n must be a positive integer"

    return sum([pow(x, 2) for x in range(n)])
