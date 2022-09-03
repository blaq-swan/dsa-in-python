#!/usr/bin/python3
"""are numbers in a sequence distinct?"""


def are_distinct(sequence) -> bool:
    """checks if numbers in a sequence are distinct
    Args:
        sequence: sequence of numbers
    Returns:
        True if numbers in sequence are distinct, False otherwise"""

    if not isinstance(sequence, (list, tuple, str, range)):
        raise TypeError("input must be a sequence")

    def count():
        """counts the occurence of a character
        Returns:
            a dictionary of items: count of items"""

        counter = {}
        for x in sequence:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1
        return counter

    for val in count().values():
        if val > 1:
            return False
        return True
