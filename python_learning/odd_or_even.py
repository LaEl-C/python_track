num = int(input("Enter number: "))

if num % 2 != 0:
    print(f"{num} is an odd number")
else: 
    print(str(num) + " is an even number")

if num % 4 == 0:
    print(f"{num} is a multiple of 4")

check = int(input("Divisor: "))
if num % check == 0:
    print(f"{check} is a factor of {num}")
    