def num_rev(num):
    res = 0
    neg = num < 0
    if neg:
        num = abs(num)
            
    while num > 0:
        res = res*10 + num % 10
        num = num//10
    if neg:
        res = -res
    return res

print(num_rev(12345))
print(num_rev(-12345))



# OR

def num_rev2(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    res = 0
    while num > 0:
        res = res * 10 + num % 10
        num = num // 10
    return sign * res

print(num_rev2(12345))    # 54321
print(num_rev2(-12345))   # -54321




# OR

def num_rev3(num):
    res = 0
    negative = num < 0
    if negative:
        num = abs(num)
    while num > 0:
        res = res * 10 + num % 10
        num = num // 10
    if negative:
        res = -res   # ✅ negate ONCE, after the loop
    return res