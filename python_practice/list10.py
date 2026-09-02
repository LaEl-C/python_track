a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Enter number: "))

# less_than= [char for char in a if char < num]
# print(less_than)


less_than = []
for char in a:
    if char < num:
        less_than.append(char)
print(less_than)













li = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = input("Enter number: ")
print([val for val in li if val < int(num)])