"""Pig Latin."""
def translate(text):
    """
    para: string
    return: string
    """
    vowels = "aeiou"
    res = ""
    for word in text.split():
        if word[0] in vowels or word[:2] in ("xr", "yt"):
            res += word + "ay "
        else:
            for i, ch in enumerate(word):
                if ch in vowels or (ch == "y" and i > 0):
                    break
            if word[i] == "u" and word[i - 1] == "q":
                i += 1
            res += word[i:] + word[:i] + "ay "
    return res.strip()   # trim trailing space