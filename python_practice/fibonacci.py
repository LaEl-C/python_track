"""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""

user_input= int(input("Enter a number: "))
a= 1
b= 0
c = []
while len(c) < user_input:
    a, b = b, a+b
    c.append(a)
print(c)





# seq= []
# while a < 1000:
#     a, b = b, a+b
#     seq.append(a)
# print(seq[:user_input])





def fibonnaci(number):
    if number <= 1:
        return 1
    return fibonnaci(number - 1) + fibonnaci(number - 2)
# """fibonnaci(4)
# = fibonnaci(3) + fibonnaci(2)
# = (fibonnaci(2) + fibonnaci(1)) + (fibonnaci(1) + fibonnaci(0))
# = ((fibonnaci(1) + fibonnaci(0)) + 1) + (1 + 1)
# = ((1 + 1) + 1) + 2
# = 3 + 2
# = 5"""
user_input = int(input("How many fibonnaci do you want to generate?: "))
for number in range(user_input):
    print(fibonnaci(number))