# Student Grade Calculator

def get_marks(subject, low, high):
    while True:
        try:
            mark = int(input(f"Enter the {subject} Marks: "))

            if low <= mark <= high:
                return mark
            else:
                print(f"Please enter a valid mark between {low} and {high}.")

        except ValueError:
            print("Please enter a valid mark")


def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    lowest = min(marks)
    highest = max(marks)

    return total, average, lowest, highest


def get_grade(average, marks):
    if min(marks) < 70:
        return "F"
    elif average >= 190:
        return "S"
    elif average >= 180:
        return "A+"
    elif average >= 170:
        return "A"
    elif average >= 160:
        return "B+"
    elif average >= 150:
        return "B"
    elif average >= 140:
        return "C+"
    elif average >= 130:
        return "C"
    elif average >= 120:
        return "D+"
    elif average >= 110:
        return "D"
    elif average >= 100:
        return "E+"
    elif average >= 90:
        return "E"
    elif average >= 80:
        return "J+"
    elif average >= 70:
        return "J"
    else:
        return "F"


def get_result(grade):
    if grade == "F":
        return "FAIL"
    else:
        return "PASS"


def main():
    student = input("Enter the Student Name: ")

    low = 0
    high = 200

    subjects = [
        "English",
        "Tamil",
        "Maths",
        "Physics",
        "Chemistry",
        "Computer Science"
    ]

    marks = []

    for sub in subjects:
        marks.append(get_marks(sub, low, high))

    total, average, lowest, highest = calculate_results(marks)

    grade = get_grade(average, marks)

    result = get_result(grade)

    print()
    print("+--------------------------------------------------+")
    print("|                STUDENT REPORT                    |")
    print("+--------------------------------------------------+")
    print(f"| Student Name     : {student:<30}|")
    print("+--------------------------------------------------+")

    for sub, mak in zip(subjects, marks):
        print(f"| {sub:<16} : {mak:<30}|")

    print("+--------------------------------------------------+")
    print(f"| Total Marks      : {total:<30}|")
    print(f"| Average Marks    : {average:<30.2f}|")
    print(f"| Highest Marks    : {highest:<30}|")
    print(f"| Lowest Marks     : {lowest:<30}|")
    print(f"| Grade            : {grade:<30}|")
    print(f"| Result           : {result:<30}|")
    print("+--------------------------------------------------+")

    # Final Message

    if result == "FAIL":
        print("|           Better luck next time!                 |")
    else:
        print("|          Congratulations! You Passed!            |")

    print("+--------------------------------------------------+")


if __name__ == "__main__":
    main()