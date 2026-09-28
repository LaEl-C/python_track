def equilateral(sides):
    a,b,c = sides
    return is_valid(sides) and a==b==c


def isosceles(sides):
    a,b,c = sides
    return is_valid(sides) and (a==b or b==c or a==c)


def scalene(sides):
    a,b,c = sides
    # return is_valid(sides) and (a!=b and b!=c and a!=c)
    return is_valid(sides) and len(set(sides)) == 3

def is_valid(sides):
    sides.sort()
    a,b,c = sides
    return a != 0 and a + b >= c
    # if a > 0 and b > 0 and c > 0:
    #     if a + b >= c and b + c >= a and a + c >= b:
            # return True
    # return False