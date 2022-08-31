#!/usr/bin/python3
"""odd summation module"""

def odd_squares_sum(n):
    """adds the squares of odd numbers in range n"""

    if not isinstance(n,int) and  n >= 0:
        raise TypeError("n must be a positive integer")
    return sum([(i ** 2) for i in range(n) if i % 2 == 1])


print(odd_squares_sum(10))
