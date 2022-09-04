#!/usr/bin/python3
"""printing alphabets without typing them manually"""


def alphabets():
    """generates a .. z
    Returns:
        a list containing a .. z
    """

    return [chr(x) for x in range(97, 123)]
