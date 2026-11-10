# def rebase(input_base, digits, output_base):
#     if input_base < 2:
#        raise ValueError("input base must be >= 2")
#     if output_base < 2:
#         raise ValueError("output base must be >= 2")
#     for dit in digits:
#         if dit >= input_base or dit < 0:
#             raise ValueError("all digits must satisfy 0 <= d < input base")

#     if output_base == 10:
#         return to_ten(input_base, digits, output_base)
#     if input_base == 10:
#         return from_ten(input_base, digits, output_base)
#     return from_ten(input, (to_ten(input_base, digits, output_base)), output_base)


# def to_ten(input, digit, output):
#     ans = 0
#     final_ans = []
#     for index, num in enumerate(digit):
#         lent = len(digit)
#         ind = lent - (index + 1)
#         ans += num *(input**ind)
    
#     for _ in range(len(str(ans))):
#         final_ans.insert(0, ans%10)
#         ans//=10
#     return final_ans

# def from_ten(input, digit, output):
#     deci = int("".join(str(dit) for dit in digit))
#     if deci <= 0:
#         return [0]
#     lit= []
#     while deci > 0:
#         lit.insert(0, deci%output)
#         deci//=output
#     return lit


def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # digits -> integer
    value = 0
    for d in digits:
        value = value * input_base + d

    # integer -> output_base digits
    if value == 0:
        return [0]
    result = []
    while value > 0:
        result.insert(0, value % output_base)
        value //= output_base
    return result