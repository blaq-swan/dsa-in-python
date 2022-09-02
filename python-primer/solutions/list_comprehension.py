#!/usr/bin/python3
"""implementing list comprehension"""


def powers_of_two():
    """
    exponents with a base of 2
    Returns:
        list with powe4rs of base 2
    """

    return [pow(2, x) for x in range(9)]
