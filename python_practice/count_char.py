def char_count(words):
    word = words.strip().lower().replace(" ", "")
    count = {}
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1 
    return count
print(char_count(" HeLLL  lllL L Lo "))