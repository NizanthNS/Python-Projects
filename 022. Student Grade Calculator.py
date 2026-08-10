# Student Grade Calculator

student = input("Enter the Student Name: ")

low = 0
high = 200


def get_marks(subject):
    while True:
        try:
            mark = int(input(f"Enter {subject} Marks: "))

            if low <= mark <= high:
                return mark
            else:
                print(f"Please enter a valid mark between {low} and {high}.")

        except ValueError:
            print("Please enter a valid number.")


m1 = get_marks("English")
m2 = get_marks("Tamil")
m3 = get_marks("Maths")
m4 = get_marks("Physics")
m5 = get_marks("Chemistry")
m6 = get_marks("Computer Science")


marks = [m1, m2, m3, m4, m5, m6]


total = sum(marks)
average = total / len(marks)
lowest = min(marks)
highest = max(marks)


if average >= 190:
    grade = "S"
elif average >= 180:
    grade = "A+"
elif average >= 170:
    grade = "A"
elif average >= 160:
    grade = "B+"
elif average >= 150:
    grade = "B"
elif average >= 140:
    grade = "C+"
elif average >= 130:
    grade = "C"
elif average >= 120:
    grade = "D+"
elif average >= 110:
    grade = "D"
elif average >= 100:
    grade = "E+"
elif average >= 90:
    grade = "E"
elif average >= 80:
    grade = "J+"
elif average >= 70:
    grade = "J"
else:
    grade = "F"


if lowest < 70:
    result = "FAIL"
else:
    result = "PASS"


print()
print("+--------------------------------------------------+")
print("|                STUDENT REPORT                    |")
print("+--------------------------------------------------+")
print(f"| Student Name     : {student:<30}|")
print("+--------------------------------------------------+")
print(f"| English          : {m1:<30}|")
print(f"| Tamil            : {m2:<30}|")
print(f"| Maths            : {m3:<30}|")
print(f"| Physics          : {m4:<30}|")
print(f"| Chemistry        : {m5:<30}|")
print(f"| Computer Science : {m6:<30}|")
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