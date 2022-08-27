#!/usr/bin/python3

def sum_square(n):
    square_sum = []
    count = 0
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n <= 0:
        raise ValueError("n must be positive")
    for i in range(n):
        square_sum.append(i ** 2)
    for x in square_sum:
        count += x
    return count

print(sum_square(-10))
