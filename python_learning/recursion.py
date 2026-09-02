def wash_mugs(stack_size):
    if stack_size <= 0:  # Base case catches zero and negative safety boundaries
        print("Stack is empty!\n")
        return
        
    print(f"Washing mug {stack_size}")
    wash_mugs(stack_size - 1)  # Safely approaches the base case

wash_mugs(5)



"""#Bad....no base case....system crashes
def wash_mugs(stack_size):
    print(f"Washing mug {stack_size}")
    wash_mugs(stack_size - 1)  # Keeps subtracting past zero

wash_mugs(3)"""



def count_down(cups):
    if cups <= 0:
        print("Done!\n")
        return
    print("Cup: " + str(cups))
    count_down(cups - 1)

count_down(3)



def sum_stack(mugs):
    if mugs <= 0:
        return 0
    return mugs + sum_stack(mugs - 1)

print(sum_stack(4))



def countdown(n):
    print(n)
    # How it works: It prints the number first, THEN recurses with a smaller number. This means it prints from high to low.
    # Base case to stop recursion
    if n == 0:
        return
    else:
        # Recursive call
        countdown(n - 1)

countdown(100)  # This works fine (stack depth = 1000)
# countdown(100000)  # 💥 RecursionError: maximum recursion depth exceeded


# To count up from 0 to n, we just flip the order—recurse FIRST, then print:

def countup(n):
    # print(n)
    # Base case to stop recursion
    if n == 0:
        return
    else:
        # Recursive call
        countup(n - 1)
        print(n)
        # The print position changed cause in recursion it starts from the base up. If the print is outside it , it will do it the other way round

countup(100) 





def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))




"""Example 2: This code defines a recursive function to calculate nth Fibonacci number, where each number is the sum of the two preceding ones, starting from 0 and 1."""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))




def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n-1, acc * n)

def nontail_fact(n):
    if n == 0:
        return 1
    else:
        return n * nontail_fact(n-1)
        
print(tail_fact(5))  
print(nontail_fact(5))




def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results\n\n")
tri_recursion(6)






