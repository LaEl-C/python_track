a = [1, 1, 2, 3, 5, 8, 9, 10, 10, 11, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21]
m = 3 in a
print(m)

# x= []
# for i in a:
#     for j in b:
#         if i == j and i not in x:
#             x.append(i)
# print(x)

# print(list(set(a) & set(b)))



# import random

# a = random.sample(range(1, 100), 10)
# b = random.sample(range(1, 100), 15)

# print(set([i for i in min(a,b) if i in max(a,b)]))
b= min(a,b)
c= max(a, b)
print(b)
print(c)