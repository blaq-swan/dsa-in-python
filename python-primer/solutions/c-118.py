#!/usr/bin/python3
"""implementing list comprehension"""


def mul_by_next(n):
    """multiplies an element with the next
    Args:
        n: limit
    Returns:
        list of x by x + 1
    """

    assert int(n) == n and n > 0, "limit must be a positive integer"

    return [(x + (pow(x, 2))) for x in range(n)]
