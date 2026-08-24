# Python Number Guessing Game

import random

low = 0
high = 100
w_guess = 6

is_running = True

while is_running:

    answer = random.randint(low, high)
    guesses = 0

    while guesses < w_guess:
        try:
            guess = int(input(f"Guess a number between {low} and {high}: "))

            if guess < low or guess > high:
                print("That Number is out of range")
                continue

            guesses += 1

            if guess < answer:
                print("That Number is TOO LOW! Try again")

            elif guess > answer:
                print("That Number is TOO HIGH! Try again")

            else:
                print(f"CORRECT! The Number is {answer}")
                print(f"You have Guessed {guesses} times")

                if guesses <= w_guess:
                    print("Congratulations, you won the game!")

                play_again = input("Do you want to Play Again (Y/N): ").lower()

                if play_again != "y":
                    is_running = False

                break

        except ValueError:
            print("INVALID INPUT")
            print(f"Please Enter a Number between {low} and {high}")

    else:
        print("\nGAME OVER!")
        print(f"The Number was {answer}")
        print(f"You used all {w_guess} guesses.")

        play_again = input("Do you want to Play Again (Y/N): ").lower()

        if play_again != "y":
            is_running = False

print("Thank you for playing")
