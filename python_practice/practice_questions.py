"""### *1. FizzBuzz*

* *Core Task:* Print numbers from 1 to $n$. Replace multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
* *Advanced Challenge:* Solve it *without using the modulo operator (%)*."""
def fizzy(n):
    count_3 = 0
    count_5 = 0
    
    for i in range(1, n+1):
        count_3 += 1
        count_5 += 1
        res = ""
        if count_3 == 3:
            res += "Fizz"
            count_3 = 0
        if count_5 == 5:
            res += "Buzz"
            count_5 = 0
        if res == "":
            res += str(i)
        print(res)
fizzy(15)



#OR
def fizzbuzz(n):
    count_3 = 0
    count_5 = 0
    res = []
    for i in range(1,n+1):
        count_3 += 1
        count_5 += 1
        if count_3 == 3 and count_5 == 5:
            res.append("FizzBuzz")
            count_3 = 0
            count_5 = 0
        elif count_3 == 3:
            res.append("Fizz")
            count_3 = 0
        elif count_5 == 5:
            res.append("Buzz")
            count_5 = 0
        else:
            res.append(str(i))
    return res

print(fizzbuzz(20))




