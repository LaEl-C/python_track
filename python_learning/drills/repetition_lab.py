"""
CountUp
Instructions
Implement count_up(n). Return a list of numbers from 1 to n inclusive. If n is less than 1, return an empty list. Use a loop and range."""

def count_up(n):
    if n < 1:
         return []

    up = []
    for c in range(1, n+1):
        up.append(c)
    return up

#OR

def count_up(n):
    if n < 1:
        return []
    
    up = []
    for c in range(1, n + 1):
        up = up + [c]
    return up

print(count_up(15))



"""SumMultiples
Instructions
Implement sum_multiples(limit, divisor). Return the sum of all positive numbers from 1 to limit inclusive that are divisible by divisor. If divisor is zero, return Invalid divisor. Do not use the built-in sum function."""

def sum_multiples(limit, divisor):
    if divisor == 0:
        return "Invalid divisor"

    msum = 0
    for c in range(1, limit+1):
        if c % divisor==0:
            msum += c
    return msum
#OR

def sum_multiples(limit, divisor):
    if divisor == 0:
        return "Invalid divisor"
    
    msum = 0
    for c in range(divisor, limit+1, divisor):
        msum += c
    return msum