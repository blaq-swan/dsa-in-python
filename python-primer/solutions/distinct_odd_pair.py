#!/usr/bin/python3
"""distinct odd pairs module"""

def odd_product(my_list):
    """checks for odd_product when two numbers in a sequence are multiplied
    Args: my_list
    return: pairs whose product is odd"""
    my_pair = []
    if not isinstance(my_list, (list,tuple, range)):
        raise TypeError("my_list must be a sequnce")
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if (my_list[i] * my_list[j]) % 2 == 1:
                my_pair += [(my_list[i],my_list[j])]
    return my_pair


print(odd_product(range(10)))
