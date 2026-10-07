"""Pangram"""
def is_pangram(sentence):
    """
    para: str
    return: bool
    """
    p_sentence = "".join(char for char in set(sentence.lower()) if char.isalpha())
    return len(p_sentence)==26