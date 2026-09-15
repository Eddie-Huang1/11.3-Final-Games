"""Paper scissors rock."""
# A code to be able to randomize stuff
import random
# Variables
high_score = 0
userscore = 0
robotscore = 0
round_number = 1
replay = "yes"
words = ["paper", "scissors", "rock"]

while replay.lower() == "yes":
    print("Lets play paper scissors rock, best out of three")
    print("You will be versing against the computer")

    userscore = 0
    robotscore = 0
    round_number = 1

    while round_number <= 3:
        print(f"Round number: {round_number}")
        print("Choose a symbol")
        player_symbol = input("").lower()


        if player_symbol.lower() in words:
            print("ROCK")
            print("PAPER")
            print("SCISSORS")
            print("SHOOT")
# This random input makes the computer randomly chooses between paper, scissors or rock
computer_symbol = random.choice(words)
print(f'{player_symbol} vs {computer_symbol}')
if player_symbol == computer_symbol:
    print("Tie")
elif (player_symbol == "paper" and computer_symbol == "rock") or \
(player_symbol == "scissors" and computer_symbol == "paper") or \
(player_symbol == "rock" and computer_symbol == "scissors"):
    print("You win!")
    userscore += 1
else:
    print("You lose")
    robotscore += 1

print(f'Your score {userscore} vs Computer score {robotscore}')
round_number += 1