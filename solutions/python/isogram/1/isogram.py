def is_isogram(phrase):
    isogram =  phrase.replace(" ", "").replace("-", "").lower()
    # seen = (ch for ch in isogram if ch not in seen)
    return len(isogram) == len(set(isogram))
