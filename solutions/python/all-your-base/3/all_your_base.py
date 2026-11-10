"""Number base."""
def rebase(input_base, digits, output_base):
    """
    Para: digit and list
    return: list
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for dit in digits:
        if dit >= input_base or dit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    ans = 0
    # for num in digits:
    #     ans = ans * input_base + num  #Horner's method
    
    for index, num in enumerate(digits):
        ind = len(digits) - (index + 1)
        ans += num *(input_base**ind)
        
    if ans <= 0:
        return [0]
    lit= []
    while ans > 0:
        lit.insert(0, ans%output_base)
        ans//=output_base
    return lit