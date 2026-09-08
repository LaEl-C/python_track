"""Instructions
Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
The word isograms, however, is not an isogram, because the s repeats."""

def isogram(str):
    word = str.replace("-", "").replace(" ", "").lower()
    if len(set(word)) != len(word):
        return "not an Isogram"
    else:
        return "Isogram"

print(isogram("Isograms"))
print(isogram("Isogram"))
print(isogram("Evidence"))
print(isogram(" back - ground "))




# OR

def find_isogram(word):
    word = word.lower()
    count = "" #you can use [] a dictionary instead
    for char in word:
        if char in count and char != "-" and char != " ":
            return 'This is not an isogram'
        else:
            count += char
    return 'This is an isogram'
 

print(find_isogram("Evidence"))
print(find_isogram("B    ac-kgr-o u    nd"))

