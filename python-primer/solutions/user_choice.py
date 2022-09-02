#!/usr/bin/python3
"""implementing user version of random.choice using randrange submodule"""
import random


def user_choice(sequence, step=1):
    """implements choice method
    Args:
        sequence: Non-empty sequence
        step: steps to consider
    Returns:
        Random element from sequence
    """

    if not isinstance(sequence, (str, list, tuple, range)):
        raise TypeError("sequence must be a sequence")
    if len(sequence) == 0:
        raise IndexError("sequence must not be empty")

    start, end, = 0, len(sequence)

    return sequence[random.randrange(start, end, step)]
