def palindrome(word):
    word = word.lower()
    new_word = "".join(reversed(word))
    if word == new_word:
        return True
    return False

print(palindrome("hannah"))
print(palindrome("Hello"))
print(palindrome("Tenet"))


#OR

def palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(palindrome("hannah"))  # True
print(palindrome("Hello"))   # False
print(palindrome("Tenet"))   # True


#OR

def palindrome(word):
    word = word.lower()
    new_word = "".join(reversed(word))
    return word == new_word

print(palindrome("hannah"))  # True
print(palindrome("Hello"))   # False
print(palindrome("Tenet"))   # True