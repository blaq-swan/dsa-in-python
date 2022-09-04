#!/usr/bin/python3
"""practice"""


def reversing_sequence(my_list):
    rev_list = []
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            my_list[i], my_list[j] = my_list[j], my_list[i]
            x = (my_list[i], my_list[j])
            rev_list.append(x)
    return rev_list


print(reversing_sequence([1, 2, 3, 4, 5]))
