sentence = input("Enter a sentence: ")
words = sentence.split()

def word_frequency(words):
    if len(words) == 0:
        return {}

    word = words[0]
    frequency = word_frequency(words[1:])

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

    return frequency




print(word_frequency(words))