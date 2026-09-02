number= int(input("Enter a number: "))

if number % 2 == 0:
    print("This number is even!")
if number % 4 == 0:
    print("and can divide 4!")
else:
    print("This number is odd!")



num= int(input("Enter number to divide: "))
check= int(input("Enter divisor: "))

if num % check == 0:
    print(f"{check} is a factor of {num}")
else:
    print(f"{check} is not a factor of {num}")