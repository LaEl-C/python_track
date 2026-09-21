def is_armstrong_number(number):
    number = str(number)
    num_sum = 0
    length = len(number)
    for c in number:
        num_sum += int(c) ** length
    return int(number) == num_sum