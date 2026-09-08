"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the  game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

def guess():
    import random

    a = random.randint(1, 9)

    while True:
        b = input("Your guess: ")
        try:
            b = int(b)
            if a > b:
                print("Too low!")
            elif a < b:
                print("Too High!")
            else:
                print("You got it right!!!")
                break
        except:
            print("Invalid entry. Integer Only")
        

guess()