#!/usr/bin/python3
"""minmax module"""


def minmax(data) -> tuple:
    """checks for the minimum and maximum value given a sequence of values"""
    if not isinstance(data,(list)):
        raise TypeError("data must be a list")
    max_val = data[0]
    min_val = data[0]
    for i in data:
        if not isinstance(i, (int, float)):
            raise TypeError("i must be a float or integer")
        if i >= data[0]:
            max_val = i
    for i in data:
        if i <= data[0]:
            min_val = i
    return min_val, max_val
