#!/usr/bin/python3
"""reversing a list"""


def reverse_list(my_list) -> list:
    """reverses a list of integers
    Args:
        my_list: list input
    Returns:
        reversed my_list
    """

    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list")
    for x in my_list:
        if not isinstance(x, int):
            raise TypeError("My must must be a list of integers")

    for x in range(len(my_list)):
        for y in range(x + 1, len(my_list)):
            my_list[x], my_list[y] = my_list[y], my_list[x]

    return my_list
