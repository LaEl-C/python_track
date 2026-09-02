
numbers = [1, 2, 3, 4, 5]
squares = []  # Start with empty list

for x in numbers:
    squares.append(x * x)  # Add square to list

print(squares)  # [1, 4, 9, 16, 25]

"""With List Comprehension"""

numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]



#Example 2
names = ["alice", "bob", "charlie"]
uppercase = []

for name in names:
    uppercase.append(name.upper())

print(uppercase)  # ['ALICE', 'BOB', 'CHARLIE']

"""With list comprehension"""

names = ["alice", "bob", "charlie"]
uppercase = [name.upper() for name in names]
print(uppercase)  # ['ALICE', 'BOB', 'CHARLIE']


words = ["apple", "banana", "avocado", "cherry"]
# Expected: ['apple', 'avocado']
a_words = [word for word in words if word.startswith('a')]
print(a_words)


