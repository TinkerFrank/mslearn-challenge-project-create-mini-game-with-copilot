# write 'hello world' to the console
print('hello world')

# write a rock paper scissor games where the user plays against the computer
# Path: app.py
# import the random module
import random
# create a list of play options
t = ["Rock", "Paper", "Scissors"]
# assign a random play to the computer
computer = t[random.randint(0,2)]
# set player to False
player = False
# initialize scores
player_score = 0
computer_score = 0

while player != "stop":
    # set player to True
    player = input("Rock, Paper, Scissors? (Type 'stop' to quit)")
    if player == "stop":
        break
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computer_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computer_score += 1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1
    else:
        print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[random.randint(0,2)]

# print final scores
print("Final Scores:")
print("Player:", player_score)
print("Computer:", computer_score)

