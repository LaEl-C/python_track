def countdown(n, message):
    if n < 1:
        print(message)
        return
    print (n)
    countdown(n-1, message)
    
countdown(9, "Lift Off!!!!")
