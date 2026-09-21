"""Armstrong number."""
def is_armstrong_number(number):
    """
    para = int
    return = bool
    """
    number = str(number)
    num_sum = 0
    length = len(number)
    for num in number:
        num_sum += int(num) ** length
    return int(number) == num_sum