def quad_a(x, y):
    if x <= 0 or y <= 0:
        return
    
    for row in range(1, y + 1):
        for col in range(1, x + 1):
            # Check if current position is a corner
            if (row == 1 or row == y) and (col == 1 or col == x):
                print("o", end="")
            elif row == 1 or row == y:  # Check if on top or bottom edge
                print("-", end="")
            elif col == 1 or col == x:  # Check if on left or right edge
                print("|", end="")
            else:  # Must be inside
                print(" ", end="")
        print()  # Move to next line


# Example usage
quad_a(5, 3)


# def quad_a(x, y):
#     if x <= 0 or y <= 0:
#         return
    
#     for row in range(1, y + 1):
#         line = ""
#         for col in range(1, x + 1):
#             if (row == 1 or row == y) and (col == 1 or col == x):
#                 line += "o"
#             elif row == 1 or row == y:
#                 line += "-"
#             elif col == 1 or col == x:
#                 line += "|"
#             else:
#                 line += " "
#         print(line)

# quad_a(5, 3)


def quad_b(x, y):
    if x <= 0 or y <= 0:
        return
    
    for row in range(1, y + 1):
        for col in range(1, x + 1):
            # Check if current position is a corner
            if (row == 1 and col == 1) or (row == y and col == x):
                print("/", end="")
            elif (row == 1 and col == x) or (row == y and col == 1):
                print("\\", end="")
            elif row == 1 or row == y or col == 1 or col == x:  # Check if on top or bottom edge
                print("*", end="")
            else:  # Must be inside
                print(" ", end="")
        print()  # Move to next line

quad_b(5,3)



def quad_c(x, y):
    if x <= 0 or y <= 0:
        return
    
    for row in range(1, y + 1):
        for col in range(1, x + 1):
            # Check if current position is a corner
            if row == 1 and (col == 1 or col == x):
                print("A", end="")
            elif row == y and (col == 1 or col == x):
                print("C", end="")
            elif row == 1 or row == y or col == 1 or col == x:  # Check if on top or bottom edge
                print("B", end="")
            else:  # Must be inside
                print(" ", end="")
        print()  # Move to next line

quad_c(5,3)



def quad_d(x, y):
    if x <= 0 or y <= 0:
        return
    
    for row in range(1, y + 1):
        for col in range(1, x + 1):
            # Check if current position is a corner
            if col == 1 and (row == 1 or row == y):
                print("A", end="")
            elif col == x and (row == 1 or row == y):
                print("C", end="")
            elif row == 1 or row == y or col == 1 or col == x:  # Check if on top or bottom edge
                print("B", end="")
            else:  # Must be inside
                print(" ", end="")
        print()  # Move to next line

quad_d(5,3)



def quad_e(x, y):
    if x <= 0 or y <= 0:
        return
    
    for row in range(1, y + 1):
        for col in range(1, x + 1):
            if (row == 1 and col == 1) or (row == y and col == x):
                print("A", end="")
            elif (row == 1 and col == x) or (row == y and col == 1):
                print("C", end="")
            elif row == 1 or row == y or col == 1 or col == x:
                print("B", end="")
            else:
                print(" ", end="")
        print()

quad_e(5, 3)