"""ISBN_verifier."""
def is_valid(isbn):
    """
    para = string
    return = bool
    """
    isbn = isbn.strip().replace("-", "")
    if len(isbn) != 10:
        return False

    sum_num = 0
    for ind, char in enumerate(isbn):
        if ind < 9:
            if not char.isdigit():
                return False
            num = int(char)
        else:
            if char == "X":
                num = 10
            elif char.isdigit():
                num = int(char)
            else:
                return False
        
        sum_num += num * (10-ind)

    return sum_num % 11 == 0

            