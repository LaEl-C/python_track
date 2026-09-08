"""Make a two-player Rock-Paper-Scissors  game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game) Games

Remember the rules:

Rock beats  scissors
 Scissors beats paper
Paper beats rock"""

def rps():
    Player1 = input("Rock, Paper, Scissors: ")
    Player2 = input("Rock, Paper, Scissors: ")

    Player1 = Player1.lower().strip()
    Player2 = Player2.lower().strip()

    # if Player1.lower() not in ["rock", "paper", "scissors"] or \
    #    Player2.lower() not in ["rock", "paper", "scissors"]:
    #     print("Invalid Input. Enter Rock, Paper Or Scissors")


    if Player1 == Player2:
        print("DRAW!")
        # rps()
    else:
        match(Player1, Player2):
            case ("rock", "scissors")|("scissors", "paper")|("paper", "rock"):
                print("Player1 wins!")
            case ("scissors", "rock")|("paper", "scissors")|("rock", "paper"):
                print("Player2 wins!")
            case _:
                print("Invalid Input. Enter Rock, Paper Or Scissors")
        # print(input("Replay (Y/N): "))

    if input("Replay (Y/N): ").upper() == "Y":
        print("Starting New game...")
        rps()
    else:
        print("Thanks For Playing!")
        return
    

rps()

