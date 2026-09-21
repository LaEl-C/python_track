""" Grains Exercise. """
def square(number):
    """
        para: int
        return: int
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1) 


def total():
    """
        para: int
        return: int
    """
    totals = 0
    for num in range(1, 64+1):
        totals += square(num)
    return totals
