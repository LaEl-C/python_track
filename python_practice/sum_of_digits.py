"""3 Sum of Digits
Calculate the sum of the individual digits in a positive integer.
sum_of_digits(1234) → 10
Hint: Base case: single-digit (n < 10) returns itself. Recursive step: last digit + sum_of_digits(rest).
def sum_of_digits(n):
# Base case: single-digit number
if n < 10:
return n
# Recursive step: last digit + sum of the rest
return (n % 10) + sum_of_digits(n // 10)
4 Power Function
Calculate base raised to the power of exponent recursively.
power(2, 5) → 32
Hint: Base case: exponent 0 → 1. Recursive step: base * power(base, exponent-1).
def power(base, exponent):
# Base case: anything to the power of 0 is 1
if exponent == 0:
return 1
# Recursive step: multiply base by result of smaller power
return base * power(base, exponent - 1)"""

def sum_digits(digit):
    add = 0
    for c in str(digit):
        add += int(c)
    return add

print(sum_digits(12345))


#OR
def sum_digits(digit):
    return sum(int(c) for c in str(digit))

print(sum_digits(12345))  # Output: 10


#OR
def rec_sum(num):
    add = 0
    if num//10 == 0:
        return num
    add += num%10 + rec_sum(num//10)
    return add

print(rec_sum(12345)) 