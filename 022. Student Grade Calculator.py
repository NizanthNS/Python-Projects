# Student Grade Calculator

student = input("Enter the Student Name: ")

def get_marks(subject):
    while True:
        mark = int(input(f"Enter the {subject} marks: "))

        if 0 <= mark <= 100:
            return mark
        else:
            print("Please enter a valid mark")

m1 = get_marks("English")
m2 = get_marks("Tamil")
m3 = get_marks("Math")
m4 = get_marks("Science")
m5 = get_marks("Social Science")

marks = [m1, m2, m3, m4, m5]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 50:
    grade = "E"
else:
    grade = "F"

if min(marks) < 35:
    result = "FAIL"
else:
    result = "PASS"

print("+--------------------------------+")
print("|        STUDENT REPORT          |")
print("+--------------------------------+")
print("|                                |")
print(f"|   Student Name   : {student:<12}|")
print("|                                |")
print("+--------------------------------+")

print(f"|   English        : {m1:<12}|")
print(f"|   Tamil          : {m2:<12}|")
print(f"|   Maths          : {m3:<12}|")
print(f"|   Science        : {m4:<12}|")
print(f"|   Social Science : {m5:<12}|")

print("+--------------------------------+")

print(f"|   Total Marks    : {total:<12}|")
print(f"|   Average Marks  : {average:<12.2f}|")
print(f"|   Highest Marks  : {highest:<12}|")
print(f"|   Lowest Marks   : {lowest:<12}|")
print(f"|   Grade          : {grade:<12}|")
print(f"|   Result         : {result:<12}|")

print("+--------------------------------+")

if result == "FAIL":
    print("|   Better luck next time!       |")
else:
    print("|   Congratulations! Passed!     |")

print("+--------------------------------+")