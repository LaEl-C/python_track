"""
Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
"""

range(start, stop, step)
start = int(input("Enter a start number"))
end = int(input("Enter a end number"))
if start > end:
    print("A friendly Error message")
    start = int(input("Enter a start number"))
    end = int(input("Enter a end number"))
else:
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
        else:
            print(i)




#Steps
# a function that prints the result
# a function that takes user input(Recalling)


#The function that runs when user enters a valid input
def print_result(start , end, step):
    for i in range(start, end, step): 
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
        else:
            print(i)

#The function that receives input
def receive_input():
    start = int(input("Enter a start: "))
    end = int(input("Enter the end: "))
    if start > end:
    #     print("You entered a value whose start is greater than the end")
    #     receive_input()
        print_result(start, end - 1, -1)
    else:
        print_result(start, end + 1, 1)


receive_input()



