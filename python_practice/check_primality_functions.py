"""Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below."""

user_input= int(input("input a number: "))
divi= []
for i in range(1,user_input+1):
    if user_input % i == 0:
        divi.append(i)
print(divi == [1,user_input])


#OR

def check_prime(num):
    if num <= 1:
        return 'This is not a prime number'
    
    # Check divisors up to square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 'This is not a prime number'
            
    return 'This is a prime number'

print(check_prime(12))
print(check_prime(11))

#OR

def check_prime2(num):

    if num <= 1:
        return 'This is not a prime number'

    if num == 2:
        return 'this is a prime number'

    for i in range (2, num):
        if num % i == 0:
            return 'this is not a prime number'
    else:
        return 'this is a prime number'

print(check_prime2(14))
print(check_prime2(13))


#OR

# Write a function is_prime(n) that returns True if n is a prime number, else False.
# Prime is >1 and divisible only by 1 and itself.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    i = 2
    while  i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(17))
print(is_prime(1))
print(is_prime(0))