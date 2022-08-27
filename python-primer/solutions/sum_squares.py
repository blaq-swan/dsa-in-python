#!/usr/bin/python3
"""square_sum module"""


def sum_square(n) -> int:
    """
    finds sum of the squares of all the positive integers smaller than n
    Args:
        n: number limit
    Returns:
        sum of all positive integers
    """

    square_sum = []
    count = 0
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be positive")
    for i in range(n):
        square_sum += [pow(i, 2)]
    for x in square_sum:
        count += x
    return count
