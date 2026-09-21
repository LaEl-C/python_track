def square(number):
    """This function takes a number which is the position of the square and returns how much grains are on it"""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1) 


def total():
    """This function sums up all grains on the chessboard and returns the value"""
    totals = 0
    for num in range(1, 64+1):
        totals += square(num)
    return totals
