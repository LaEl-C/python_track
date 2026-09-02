"""FirstAndLast
Instructions
Implement first_and_last(value). Return a dictionary with two keys: "first" and "last". "first" should contain the first character of the string. "last" should contain the last character of the string. If the string is empty, return {"first": "", "last": ""}."""

def first_and_last(value):
    dictionary = {
        "first": "",
        "last": ""
    }

    if value == "":
        return dictionary
    else:
        dictionary["first"] = value[0]
        dictionary["last"] = value[-1]
    return dictionary

#OR

def first_and_last(value):
    if value == "":
        return {"first": "", "last": ""}
    else:
        return {"first": value[0], "last": value[-1]}

#OR

def first_and_last(value):
    if not value:  # Same as checking if value == ""
        return {"first": "", "last": ""}
    return {"first": value[0], "last": value[-1]}

"""CleanUsername
Instructions
Implement clean_username(value). The function should remove leading and trailing spaces, convert the text to lowercase, and replace every space with an underscore. Return the cleaned username."""

def clean_username(value):
    value = value.strip()
    value = value.lower()
    value = value.replace(" ", "_")

    return value

#OR

def clean_username(value):
    return value.strip().lower().replace(" ", "_")

"""ManualStringLength
Instructions
Implement str_len(value) without using len(). Count the characters manually and return the number of characters in the string."""

def str_len(value):
    count = 0
    for i in value:
        count += 1
    
    return count

"""ReverseString
Instructions
Implement reverse_string(value) without using slicing shorthand like [::-1]. Return a new string containing the input characters in reverse order."""

def reverse_string(value):
    s = ""
    for i in value:
        s = i + s 
    return s

#OR

def reverse_string(value):
    return value[::-1]

#OR

def reverse_string(value):
    return value[5::-1]

"""CensorWords
Tests passed ✓
Instructions
Implement censor_words(text, banned_word). Return a new string where every occurrence of banned_word is replaced with "***". The match is case-sensitive. Do not use import or regular expressions."""

def censor_words(text, banned_word):
    return text.replace(banned_word, "***")
    