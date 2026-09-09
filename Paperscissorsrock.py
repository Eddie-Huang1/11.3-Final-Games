"""Paper scissors rock."""
# A code to be able to randomize stuff
import random
# Variables
high_score = 0
userscore = 0
robotscore = 0
symbol_dictionary = ["paper", "scissors", "rock"]

print("Lets play paper scissors rock, best out of three")
print("You will be versing against the computer")
print("Choose a symbol")
player_symbol = input("")
if player_symbol.lower() == "paper":
    print("ROCK")
    print("PAPER")
    print("SCISSORS")
    print("SHOOT")
# This random input makes the computer randomly chooses between paper, scissors or rock
computer_symbol = random.choice(symbol_dictionary)
print(f'{player_symbol} vs {computer_symbol}')
if player_symbol == computer_symbol:
    print("Tie")