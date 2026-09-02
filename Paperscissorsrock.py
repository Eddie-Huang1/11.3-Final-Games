"""Paper scissors rock."""
# A code to be able to randomize stuff
import random
# Variables 
high_score = 0
userscore = 0
robotscore = 0
symbol_list = ["paper", "scissors", "rock"]

print("Lets play paper scissors rock, best out of three")
print("You will be versing against the computer")
print("Choose a symbol")
symbol = input("")
if symbol.lower() == "paper" or "rock" or "scissors":
    print("Paper")
    print("Scissors")
    print("Rock")