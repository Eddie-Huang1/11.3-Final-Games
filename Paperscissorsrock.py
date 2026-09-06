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
symbol = input("")
if symbol.lower() == "paper":
    print("ROCK")
    print("PAPER")
    print("SCISSORS")
    print("SHOOT")
# This random input makes the computer randomly chooses between paper, scissors or rock
random_symbol = random.choice(symbol_dictionary)
print(random_symbol)
print(symbol)
print(f'{symbol} vs {random_symbol}')