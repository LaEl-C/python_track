def guess():
    import random

    while True:  # Outer loop for replay
        a = random.randint(1, 9)
        guess_counter = 0

        while True:  # Inner loop for guessing
            b = input("Guess the Number (or 'exit' to quit): ")
            
            # Check for exit FIRST
            if b.lower() == "exit":
                print(f"You made {guess_counter} guesses before exiting.")
                return  # Exit the entire function

            try:
                b = int(b)
                guess_counter += 1  # Only count valid numbers

                if a > b:
                    print("Too low!")
                elif a < b:
                    print("Too high!")
                else:
                    print(f"You got it right in {guess_counter} guesses!!!")
                    break  # Exit inner loop when correct

            except ValueError:
                print("Invalid entry. Please enter an integer or 'exit'.")

        # Ask to play again
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break  # Exit outer loop
        else:
            print("\n--- New Game Started! ---\n")
            # Outer loop will restart with new random number and reset counter

guess()