# Student Marks Analyzer

def get_marks(subject, low, high):
    while True:
        try:
            mark = int(input(f"Enter the {subject} Marks:"))

            if low <= mark <= high:
                return mark
            else:
                print(f"Please enter a valid mark between {low} and {high}")

        except ValueError:
            print(f"Please enter a valid number")

def calculate_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest

def get_result(passed, failed, marks):
    for mark in marks:
        if mark >= 40:
            passed += 1
        else:
            failed += 1

    return passed, failed

def get_highest_lowest_subject(subjects, marks):
    highest_mark = max(marks)
    lowest_mark = min(marks)

    highest_subject = None
    lowest_subject = None

    for subject, mark in zip(subjects, marks):
        if mark == highest_mark:
            highest_subject = subject

        if mark == lowest_mark:
            lowest_subject = subject

    return highest_subject, lowest_subject


def main():
    student = input("Enter the name of the student: ")

    low = 0
    high = 100

    passed = 0
    failed = 0

    subjects = [
        "English",
        "Tamil",
        "Maths",
        "Science",
        "Social Science"
    ]

    marks = []

    for sub in subjects:
        marks.append(get_marks(sub, low, high))

    total, average, highest, lowest = calculate_marks(marks)

    passed, failed = get_result(passed, failed, marks)

    highest_subject, lowest_subject = get_highest_lowest_subject(subjects, marks)

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
    print(f"| Highest Subject  : {highest_subject:<30}|")
    print(f"| Lowest Marks     : {lowest:<30}|")
    print(f"| Lowest Subject   : {lowest_subject:<30}|")
    print(f"| Passed           : {passed:<30}|")
    print(f"| Failed           : {failed:<30}|")
    print("+--------------------------------------------------+")

if __name__ == "__main__":
    main()