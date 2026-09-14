"""Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates. 
Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function."""

def nodups(duplist):
    duplist = list(set(duplist))
    return duplist

print(nodups([1,2,2,3,4,6,7,8,5,6,4,6]))


def no_dups(dup_list):
    new_list = []
    for num in dup_list:
        if num not in new_list:
            new_list.append(num)
    return new_list

print(no_dups([1,2,2,3,4,6,7,8,5,6,4,6]))
# These 2 are not ordered



# OR
def no_dup_s(dup_list):
    return list(dict.fromkeys(dup_list))
print(no_dup_s([1,2,2,3,4,6,7,8,5,6,4,6]))
    