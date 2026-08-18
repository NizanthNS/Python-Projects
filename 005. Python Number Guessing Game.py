# Python Number Guessing Game

import random

low = 0
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

while is_running:
    try:
        guess = int(input(f"Guess a number between {low} and {high}: "))

        guesses += 1

        if guess < low or guess > high:
            print("That Number is out of range")

        elif guess < answer:
            print("That Number is TOO LOW! Try again")

        elif guess > answer:
            print("That Number is TOO HIGH! Try again")

        else:
            print(f"CORRECT! The Number is {answer}")
            print(f"You have Guessed {guesses} times")

            play_again = input("Do you want to Play Again (Y/N): ").lower()

            if play_again != "y":
                is_running = False
            else:
                answer = random.randint(low, high)
                guesses = 0

    except ValueError:
        print("INVALID INPUT")
        print(f"Please Enter a Number between {low} and {high}")

print("Thank you for playing")