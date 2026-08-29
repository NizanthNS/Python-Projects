# Student Records

def get_age():
    while True:
        try:
            age = int(input("Enter the Student Age: "))

            if 15 <= age <= 25:
                return age
            else:
                print("Age must be between 15 and 25")

        except ValueError:
            print("Please Enter a Valid Number")

def get_student_details():

    name = input("Enter the Student Name: ")
    age = get_age()
    course = input("Enter the Student Course: ")

    student = {
                "Name"  : name,
                "Age"   : age,
                "Course": course
               }

    return student

def display_students(students, avg_age, total_student, oldest_age, oldest_name, youngest_age, youngest_name):

    print()
    print("+--------------------------------------------------+")
    print("|                 STUDENT RECORDS                  |")
    print("+--------------------------------------------------+")

    for student in students:
        print(f"| Name        : {student['Name']:<35}|")
        print(f"| Age         : {student['Age']:<35}|")
        print(f"| Course      : {student['Course']:<35}|")
        print("+--------------------------------------------------+")
    print(f"| Average Age    : {avg_age:<32.2f}|")
    print(f"| Total Students : {total_student:<32}|")
    print(f"| Youngest S Age : {youngest_age:<32}|")
    print(f"| Youngest S Name: {youngest_name:<32}|")
    print(f"| Oldest S Age   : {oldest_age:<32}|")
    print(f"| Oldest S Name  : {oldest_name:<32}|")
    print("+--------------------------------------------------+")

def average_age(students):
    total_age = 0

    for student in students:
        total_age += student["Age"]

    avg_age = total_age / len(students)

    return avg_age

def total_students(students):
    total_student = 0

    for student in students:
        total_student += 1

    return total_student

def category(students):
    oldest_age = students[0]['Age']
    oldest_name = students[0]['Name']
    youngest_age = students[0]['Age']
    youngest_name = students[0]['Name']

    for student in students:
        if student['Age'] > oldest_age:
            oldest_age = student['Age']
            oldest_name = student['Name']

    for student in students:
        if student['Age'] < youngest_age:
            youngest_age = student['Age']
            youngest_name = student['Name']

    return oldest_age, oldest_name, youngest_age, youngest_name

def main():

    students = []

    for i in range(3):

        print()
        print(f"Enter Details for the Student: {i + 1}")
        print("--------------------------------")

        student = get_student_details()
        students.append(student)

    avg_age = average_age(students)

    total_student = total_students(students)

    oldest_age, oldest_name, youngest_age, youngest_name = category(students)

    display_students(students, avg_age, total_student, oldest_age, oldest_name, youngest_age, youngest_name)

if __name__ == "__main__":
    main()
