def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    sum_factors = 0
    num = 1
    while num < number:
        if number%num == 0:
            sum_factors += num
        num += 1
    return "perfect" if sum_factors==number else "abundant" if sum_factors > number else "deficient"