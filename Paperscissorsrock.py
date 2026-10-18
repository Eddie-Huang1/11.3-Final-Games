"""Paper scissors rock"""
import random

# Variables
replay = "yes"
words = ["paper", "scissors", "rock"]
# While loop to make the replay work
while replay.lower() == "yes":
    print("Welcome!")
    print("Lets play paper scissors rock, best out of ten")
    print("You will be versing against the computer")
    userscore = 0
    robotscore = 0
    # For loop to make 10 rounds
    for round_number in range(1, 11):
        print(f"Round number: {round_number}")
        print("Choose a symbol")
        player_symbol = input("").lower()
        # Correct input outputs the starting phrase
        if player_symbol in words:
            print("ROCK")
            print("PAPER")
            print("SCISSORS")
            print("SHOOT")
            # random.choice(words) makes the computer choice be random
            computer_symbol = random.choice(words)
            print(f"{player_symbol} vs {computer_symbol}")
            # The results of the battle
            if player_symbol == computer_symbol:
                print("Tie")
            elif (player_symbol == "paper" and computer_symbol == "rock") or \
                 (player_symbol == "scissors" and computer_symbol == "paper") or \
                 (player_symbol == "rock" and computer_symbol == "scissors"):
                print("You win this round!")
                userscore += 1
            else:
                print("You lose this round")
                robotscore += 1
                # F strings are there to put the scores in
            print(f"Your total score: {userscore} vs Computer total score: {robotscore}")
        else:
            print("Put a symbol in.")
# Shows who the winner is
    if userscore > robotscore:
        print("VICTORY")
    elif robotscore > userscore:
        print("DEFEAT")
    else:
        print("It was a tie between you two")
# Replay is empty because if it was yes or no then it won't work
    replay = ""
    while replay != "yes" and replay != "no":
        replay = input("Do you want to play again? (yes or no): ").lower()
    if replay != "yes" and replay != "no":
        print("Put yes or no")