import random

x = [1, 2, 3]
y = [5, 10, 15]
allproducts = [a*b for a in x for b in y]
customlist = [a*b for a in x for b in y if a*b%2 != 0]
addlist = [a+b for a in x for b in y if b%3 != 0]

print(allproducts)
print(customlist)
print(addlist)

# This line of code will leave a containing a list of 5 random numbers from 0 to 99.
a = random.sample(range(100), 5)
print(a)
