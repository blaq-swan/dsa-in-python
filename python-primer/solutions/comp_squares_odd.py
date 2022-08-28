#!/usr/bin/python3
"""sum all odd squares"""


def sum_odd_sqaures(n) -> int:
    """sums all odd sqaures less than n
    Args:
        n: number limit
    Returns:
        sum of all odd squares"""

    assert int(n) == n and n >= 0, "input must be a positive integer"

    return sum(pow(x, 2) for x in range(n) if x & 1 == 1)
