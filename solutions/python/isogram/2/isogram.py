"""Isogram."""
def is_isogram(phrase):
    """
    para = str
    return = bool
    """
    cleaned = phrase.replace(" ", "").replace("-", "").lower()
    return len(cleaned) == len(set(cleaned))