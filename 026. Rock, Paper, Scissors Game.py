# Rock, Paper, Scissors Game

import random

options = ("rock", "paper", "scissors")
running = True

player_score = 0
computer_score = 0

print()
print("+=====================================+")
print("|       ROCK PAPER SCISSORS GAME      |")
print("+=====================================+")

while running:

    print()
    print("+-------------------------------------+")
    print("|              NEW ROUND              |")
    print("+-------------------------------------+")

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your Choice (ROCK, PAPER, SCISSORS): ").lower()

    print()
    print("+-------------------------------------+")
    print(f"|  Player   : {player:<24}|")
    print(f"|  Computer : {computer:<24}|")
    print("+-------------------------------------+")

    if player == computer:
        print("|              DRAW!                  |")

    elif player == "rock" and computer == "scissors":
        print("|            YOU WIN!                 |")
        player_score += 1

    elif player == "paper" and computer == "rock":
        print("|            YOU WIN!                 |")
        player_score += 1

    elif player == "scissors" and computer == "paper":
        print("|            YOU WIN!                 |")
        player_score += 1

    else:
        print("|            YOU LOSE :(              |")
        computer_score += 1

    print("+-------------------------------------+")
    print(f"|  Player Score   : {player_score:<18}|")
    print(f"|  Computer Score : {computer_score:<18}|")
    print("+-------------------------------------+")

    print()
    play_again = input("  Do You want to play again? (Y/N): ").lower()

    if play_again != "y":
        running = False


print()
print("+=====================================+")
print("|            FINAL SCORE              |")
print("+=====================================+")
print(f"|  Player Score   : {player_score:<18}|")
print(f"|  Computer Score : {computer_score:<18}|")
print("+=====================================+")

if player_score > computer_score:
    print("|       🏆 YOU ARE THE WINNER!        |")
elif computer_score > player_score:
    print("|         💻 COMPUTER WINS!           |")
else:
    print("|              DRAW!                  |")

print("+=====================================+")
print("|       Thank YOU For Playing         |")
print("+=====================================+")