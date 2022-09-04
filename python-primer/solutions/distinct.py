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

    def check_elements():
        """checks the uniqueness of frequencies
        Returns:
            True if same, False otherwise
        """

        checker = list(count().values())
        n = len(checker)
        for i in range(1, n):
            if checker[i] != checker[0]:
                return False
        return True

    return check_elements()
