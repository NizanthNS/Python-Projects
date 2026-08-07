# Python Number Guessing Game

import random

low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low} and {high}")

while True:
    guess = input(f"Guess a number between {low} and {high}: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("That number is out of the range")
        elif guess < answer:
            print("That number is too Low")
        elif guess > answer:
            print("That number is too High")
        else:
            print(f"CORRECT ANSWER!, The answer is {answer}")
            print(f"You have guessed {guesses} times")
    else:
        print("INVALID INPUT")
        print(f"Please enter a number between {low} and {high}")

    if guess == answer:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if not play_again == "y":
            is_running = False
print("Thank you for playing")