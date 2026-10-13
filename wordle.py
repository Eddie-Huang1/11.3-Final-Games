"""Wordle."""
import random
# Variables
words = ["ANGER", "BEACH", "WATER", "WORLD", "ADAPT"]
guess_word = random.choice(words)
attempts = 6

while attempts > 6:
    print("Guess the word: ")
    guess = input("").upper()
    # The lens count how much letters there
    if len(guess) > 5:
        print("Invalid, input a 5 letter word")
    