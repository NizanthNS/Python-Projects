# Python Quiz Game

questions = ("What is the capital of India?: ",
             "How many days are there in a week?: ",
             "Which planet do we live on?: ",
             "How many legs does a spider have?: ",
             "What is 10 + 5?: ")

options = (("A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"),
           ("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. Mars", "B. Venus", "C. Earth", "D. Jupiter"),
           ("A. 6", "B. 8", "C. 10", "D. 12"),
           ("A. 10", "B. 15", "C. 20", "D. 25"))

answers = ("B", "C", "C", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("WRONG")
        print(f"{answers[question_num]} is the CORRECT ANSWER.")
    question_num += 1

print("-------------------------------------")
print("               RESULTS               ")
print("-------------------------------------")

print("Answers: ", end = " ")
for answer in answers:
    print(answer, end = " ")
print()

print("Guesses: ", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()

score = score / len(answers) * 100
print(f"Your Final Score is {score}%")