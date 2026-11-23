"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 2
SUPERLIST = 3
EQUAL = 1
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return 1
    if is_sublist(list_one, list_two):
        return 2
    if is_sublist(list_two, list_one):
        return 3
    else:
        return 4


def is_sublist(one, two):
    if one == []:
        return True
    for num in range(len(two) - len(one) + 1):
        if one == two[num: num + len(one)]:
            return True
    return False
# def _is_sublist(a, b):
#     if not a:
#         return True
#     len_a, len_b = len(a), len(b)
#     return any(a == b[i : i + len_a] for i in range(len_b - len_a + 1))    

