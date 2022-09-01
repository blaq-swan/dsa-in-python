#!/usr/bin/python3
"""Proving the correlation of negative and psotive indexing"""


"""
string = s
s[k] = -n <= k < 0
    k is less than 0
        k is the index to be used

    case:
        length = 10
            last element = index 9
            To access last element:
                a. s[9] (s[k])
                b. s[-1] (s[-k])
                    constants:
        In other words:
            s[len - 1] -> last element
                s[len - 1] = s[-1]
                Therefore:
                    -n <= k < 0
        In case where s[j], with j >= 0:
            j >= 0 < n -> n >= j > 0

    Ans:
        n >= j > 0
"""
