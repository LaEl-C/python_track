"""Rotational cipher."""
def rotate(text, key):
    """
    para: str, int
    return: str
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    n_text = ""
    for ch in text:
        cap = ch.isupper()
        if ch.isalpha():
            position= (alpha.index(ch.lower())+key)%26
            if cap:
                n_text += alpha[position].upper()
            else:
                n_text += alpha[position]
        else:
            n_text += ch
    return n_text
print(rotate("Divine", 4))

#OR

"""Rotational cipher."""
def rot(text, key):
    """
    para: str, int
    return: str
    """
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n_text = ""
    for ch in text:
        if ch.isalpha() and ch.isupper():
            pos = (alpha_upper.index(ch) + key) % 26
            n_text += alpha_upper[pos]
        elif ch.isalpha():
            pos = (alpha_lower.index(ch) + key) % 26
            n_text += alpha_lower[pos]
        else:
            n_text += ch
    return n_text

print(rot("dIvInE", 7))