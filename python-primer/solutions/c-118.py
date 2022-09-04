#!/usr/bin/python3
"""implementing list comprehension"""


def mul_by_next(n):
    """multiplies an element with the next
    Args:
        n: limit
    Returns:
        list of x by x + 1
    """

    return [(x + (pow(x, 2))) for x in range(n)]
