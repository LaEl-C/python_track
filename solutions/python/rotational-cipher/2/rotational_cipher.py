"""Rotational cipher."""
def rotate(text, key):
    """
    para: str, int
    return: str
    """
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n_text = ""
    for char in text:
        # # cap = char.isupper()
        # if ch.isalpha():
        #     position= (alpha.index(char.lower())+key)%26
        #     if cap:
        #         n_text += alpha[position].upper()
        #     else:
        #         n_text += alpha[position]
        # else:
        #     n_text += char
        if char.isalpha() and char.isupper():
            pos = (alpha_upper.index(char) + key) % 26
            n_text += alpha_upper[pos]
        elif char.isalpha():
            pos = (alpha_lower.index(char) + key) % 26
            n_text += alpha_lower[pos]
        else:
            n_text += char
    return n_text