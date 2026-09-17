"""Paper scissors rock"""
import random

# Variables
high_score = 0
userscore = 0
robotscore = 0
round_number = 1
replay = "yes"
words = ["paper", "scissors", "rock"]

while replay.lower() == "yes":
    print("Lets play paper scissors rock, best out of ten")
    print("You will be versing against the computer")
    userscore = 0
    robotscore = 0
    round_number = 1
    
    while round_number <= 10:
        print(f"Round number: {round_number}")
        print("Choose a symbol")
        player_symbol = input("").lower()
        
        if player_symbol in words:
            print("ROCK")
            print("PAPER")
            print("SCISSORS")
            print("SHOOT")
            
            computer_symbol = random.choice(words)
            print(f"{player_symbol} vs {computer_symbol}")
            
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
                
            print(f"Your total score: {userscore} vs Computer total score: {robotscore}")
            round_number += 1
        else:
            print("Put a symbol in.")

    replay = input("Do you want to play again? (yes or no): ").lower()