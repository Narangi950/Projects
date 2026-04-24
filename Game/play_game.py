import random
from utils import options
def play_game():

    user = input("Enter stone/paper/scissors: ").lower()
    computer = random.choice(options)

    print("Computer chose:", computer)

    if user == computer:
        print("Match Draw")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
    else:
        print("Computer Wins!")