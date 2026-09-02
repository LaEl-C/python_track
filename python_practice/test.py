for j in range(6):
    for i in range(7):
        if ((j == 0 and i % 3 != 0) or
            (j == 1 and i % 3 == 0) or
            (j - i == 2) or
            (j + i == 8)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()