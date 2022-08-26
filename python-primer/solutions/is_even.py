#!/usr/bin/python3
"""even or not"""


def is_even(num) -> bool:
    """checks if a number is even or not using bitwise
    Args:
        num: number to be checked
    Returns: True if num is even, otherwise False
    """

    if not isinstance(num, int):
        raise TypeError("num ")
    return True if num & 1 == 0 else False
