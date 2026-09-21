# Hangman Python Program

# import random
#
# words = ("apple", "banana", "cherry", "grape", "mango")
#
# hangman_art =  {0: ("   ",
#                     "   ",
#                     "   "),
#                 1: (" o ",
#                     "   ",
#                     "   "),
#                 2: (" o ",
#                     " | ",
#                     "   "),
#                 3: (" o ",
#                     "/| ",
#                     "   "),
#                 4: (" o ",
#                     "/|\\",
#                     "   "),
#                 5: (" o ",
#                     "/|\\",
#                     "/  "),
#                 6: (" o ",
#                     "/|\\",
#                     "/ \\")}
#
# def display_man(wrong_guesses):
#     for line in hangman_art[wrong_guesses]:
#         print(line)
#
# def display_hint(hint):
#     print(" ".join(hint))
#
# def display_answer(answer):
#     print(" ".join(answer))
#
# def main():
#     answer = random.choice(words)
#     hint = ["_"] * len(answer)
#     wrong_guesses = 0
#     guessed_letters = set()
#     is_running = True
#
#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#
#         guess = input("Guess a Letter: ").lower()
#
#         if len(guess) != 1 or not guess.isalpha():
#             print("INVALID INPUT")
#             continue
#
#         if guess in guessed_letters:
#             print(f"{guess} is Already Guessed")
#             continue
#
#         guessed_letters.add(guess)
#
#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
#         else:
#             wrong_guesses += 1
#
#         if "_" not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU WIN")
#             is_running = False
#
#         elif wrong_guesses >= len(hangman_art) - 1:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU LOSE")
#             is_running = False
#
# if __name__ == "__main__":
#     main()

# Hangman Python Program - Cool Decorations

import random

words = ("apple", "banana", "cherry", "grape", "mango")

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    print("╔══════════════════════════════════════╗")
    print("║             🎮 HANGMAN 🎮            ║")
    print("╚══════════════════════════════════════╝")
    print()

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        print()
        print(f"❌ Wrong Guesses: {wrong_guesses} / 6")
        print(f"🔤 Guessed: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print()

        guess = input("🎯 Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input!")
            print("   Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"🔁 '{guess}' has already been guessed!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

            print("✅ Nice! You found a letter!")

        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)

            print()
            print("╔══════════════════════════════════════╗")
            print("║             🎉 YOU WIN! 🎉           ║")
            print("╚══════════════════════════════════════╝")
            print()
            print("        ⭐ CONGRATULATIONS! ⭐")
            print()
            print(f"        Wrong Guesses: {wrong_guesses} / 6")
            print()

            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)

            print()
            print("╔══════════════════════════════════════╗")
            print("║            💀 GAME OVER 💀           ║")
            print("╚══════════════════════════════════════╝")
            print()
            print("        Better luck next time! 😄")
            print()

            is_running = False


if __name__ == "__main__":
    main()