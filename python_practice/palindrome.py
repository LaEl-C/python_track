def palindrome(word):
    new_word = reversed(word)
    if word == new_word:
        return True

print(palindrome("hannah"))