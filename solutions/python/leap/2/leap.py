"""Leap Year."""
def leap_year(year):
    """
    Para:
    input = int
    output = bool
    """
    if year % 4 !=0:
        return False
    if (year % 4 == 0) and (year % 100 == 0) and (year % 400 != 0):
        return False
    return True

# def leap_year(year):
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#     return False