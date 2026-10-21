"""Wordle."""
import random
# Variables
words = ["ANGER", "BEACH", "GREAT", "WEIRD"
"STEAK", "TALES", "WATER", "WORLD", "ADAPT"]
guess_word = random.choice(words)
attempts = 6
# The color code
green = '\033[32m]'
red = '\033[31m]'
# Def function to make the wordle rounds work
def wordle(words, attempts = 6):
# While loop to make the attempts work
    while attempts > 0:
        print("WORDLE")
        print(f'You have {attempts} amount of attempts')
        print("Guess the 5 letter word: ")
guess = input("").upper()
# Lens is to count how many letters there are
if len(guess) == 5:
    for i in guess():
        
else:
    len(guess) != 5:
    print("Invalid, input a 5 letter word")
# Correctly guessed the word in the attempts range
if guess == guess_word:
    print("CORRECT!")