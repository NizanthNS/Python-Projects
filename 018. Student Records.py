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

def display_students(students):

    print()
    print("+--------------------------------------------------+")
    print("|                 STUDENT RECORDS                  |")
    print("+--------------------------------------------------+")

    for student in students:
        print(f"| Name   : {student['Name']:<40}|")
        print(f"| Age    : {student['Age']:<40}|")
        print(f"| Course : {student['Course']:<40}|")
        print("+--------------------------------------------------+")
    print("+--------------------------------------------------+")

def main():

    students = []

    for i in range(2):

        print()
        print(f"Enter Details for the Student: {i + 1}")
        print("------------------------------------")

        student = get_student_details()
        students.append(student)

    display_students(students)

if __name__ == "__main__":
    main()

