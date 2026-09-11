"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function."""

a = [5, 10, 15, 20, 25]
# b = []
b = [ch for ch in a if ch == a[0] or ch == a[len(a)-1]]
# for i in a:
#     if i == a[0] or i == a[-1]:
#         b.append(i)
print(b)


def first_and_last(numbers):
    return [numbers[0], numbers[-1]]

user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

print(first_and_last(numbers))