#!/usr/bin/python3
"""what about we sum the squares of all odd numbers"""


def sum_odd_squares(n) -> int:
    """sums squares of all odd numbers less than n
    Args:
        n: number limit
    Returns:
        sum of sqaures of all odd numbers less than n
        """

    assert int(n) == n and n >= 0, "input must be a positive integer"

    count = 0

    for num in range(n):
        if num & 1 == 1:
            count += pow(num, 2)
    return count
