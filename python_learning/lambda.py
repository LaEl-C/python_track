# def add(x, y):
#     return x + y

# result = add(54, 78)
# print(result)  # 8


add = lambda x, y: x + y

result = add(5, 3)
print(result)  # 8


numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8]

# Step-by-step breakdown:
# Step 1: numbers = [1, 2, 3, 4]
# Just a list of numbers.

# Step 2: lambda x: x * 2
# This is a mini-function that takes a number (x) and multiplies it by 2.

# Step 3: map(lambda x: x * 2, numbers)
# map() goes through each item in numbers and applies the lambda function to it:

# Step 4: list(map(...))
# map() returns a "map object" (not a list), so we wrap it in list() to convert it back to a list.

# Step 5: [2, 4, 6, 8] is printed.


numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

"""Step 1: numbers = [1, 2, 3, 4, 5, 6]
A list of numbers.

Step 2: lambda x: x % 2 == 0
This checks if a number is even:

% means "remainder after division"

x % 2 == 0 means "is the remainder when divided by 2 equal to 0?"

If yes → True (keep it)

If no → False (discard it)

Step 3: filter(lambda x: x % 2 == 0, numbers)
filter() checks each item and only keeps the ones where the lambda returns True:

Step 4: list(filter(...)) converts the filtered results to a list.

Step 5: [2, 4, 6] is printed.




Alternative function

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)  # [2, 4, 6]
"""


people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
people.sort(key=lambda person: person[1])  # Sort by age
print(people)  # [('Charlie', 20), ('Alice', 25), ('Bob', 30)]


"""Step 1: people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
A list of tuples. Each tuple has: (name, age)

Step 2: lambda person: person[1]
This lambda takes a person (a tuple) and returns the second item (person[1]), which is the age.

Step 3: people.sort(key=lambda person: person[1])
.sort() sorts the list, but instead of comparing the whole tuples, it uses the key to decide what to compare:

Person	Lambda returns (age)	Sort order
("Alice", 25)	25	Middle
("Bob", 30)	30	Last
("Charlie", 20)	20	First
Python sorts by the ages: 20, 25, 30

Step 4: The list is reordered to [('Charlie', 20), ('Alice', 25), ('Bob', 30)]


Alternative function

def get_age(person):
    return person[1]  # Return the age

people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
people.sort(key=get_age)
print(people)  # [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
"""



menu_items = [
    {"name": "Mocha", "price": 5.00},
    {"name": "Espresso", "price": 3.50},
    {"name": "Latte", "price": 4.50}
]

# Sort the items based on their price dictionary key
sorted_by_price = sorted(menu_items, key=lambda item: item["price"])
print(sorted_by_price)



""" sort() doesn't take the list as an argument (it's called on the list)

 sort() returns None, so sorted_by_price will be None"""

menu_items = [
    {"name": "Mocha", "price": 5.00},
    {"name": "Espresso", "price": 3.50},
    {"name": "Latte", "price": 4.50}
]

menu_items.sort(key=lambda item: item["price"])
print(menu_items)



prices = [3.0, 4.0]

# Write the lambda directly inside the map call. It has no name and is discarded afterward.
updated_prices = list(map(lambda x: x + 1, prices))
print(updated_prices)



triple = lambda x: x * 3
print(triple(5))
print(triple(15))



check_size = lambda ounces: "large" if ounces >= 16 else "small"
print(check_size(12))
print(check_size(16))




from functools import reduce
a = [1, 2, 3, 4]
mul = reduce(lambda x, y: x * y, a)
print(mul)