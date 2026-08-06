# Student Grade Calculator

name = input("Enter Student Name: ")
m1 = int(input("Enter English Marks: "))
m2 = int(input("Enter Maths Marks: "))
m3 = int(input("Enter Science Marks: "))
m4 = int(input("Enter Social Marks: "))
m5 = int(input("Enter Computer Marks: "))

marks = [m1, m2, m3, m4, m5]

total = sum(marks)
average = total / len(marks)
high = max(marks)
low = min(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

result = "Pass" if grade != "F" else "Fail"

print("------------------------")
print("    STUDENT REPORT      ")
print("------------------------")
print(f"Student Name : {name}")
print(f"Total Marks  : {total}")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
print(f"Result       : {result}")
print(f"Highest Mark : {high}")
print(f"Lowest Mark  : {low}")
print("------------------------")

if grade == "F":
    print("Better luck next time.")
else:
    print("Congratulations! You passed.")