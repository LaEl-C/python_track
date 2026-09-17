"""Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string: Programming

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me."""

def reverse_word(sentence):
    new_sentence = sentence.split()
    new_sentence.reverse()
    return " ".join(new_sentence)
print (reverse_word("Mary had a little lamb"))


#Or

def reverse_words2(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_words2("Mary had a little lamb"))
# lamb little a had Mary