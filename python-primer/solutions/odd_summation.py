#!/usr/bin/python3
"""odd summation module"""

def odd_squares_sum(n):
    """adds the squares of odd numbers in range n"""

    count = 0
    odd_sum = []
    if not isinstance(n,int) and  n >= 0:
        raise TypeError("n must be a positive integer")
    for x in range(n):
        if x % 2 == 1:
            odd_sum += [x ** 2]
    for i in odd_sum:
        count += i
    return count

print(odd_squares_sum(10))
