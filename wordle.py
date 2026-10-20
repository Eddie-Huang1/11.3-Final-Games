"""Wordle."""
import random
# Variables
words = ["ANGER", "BEACH", "GREAT", "WEIRD"
"STEAK", "TALES", "WATER", "WORLD", "ADAPT"]
guess_word = random.choice(words)
guess = ""
attempts = 6
green = '\033[32m]'

def wordle():
# While loop to make the attempts work
    while attempts == 6:
        print("Guess the word: ")
guess = input("").upper()
# For loop to add the attempts together
for attempt in attempts(1, attempts, +1):
    print("")
# Lens is to count how many letters there are
    if len(guess) > 5:
        print("Invalid, input a 5 letter word")