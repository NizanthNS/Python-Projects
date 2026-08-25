# Student Contact Manager

def get_student_details():
    name = input("Enter Student Name: ")
    age = get_age()
    course = input("Enter Student Course: ")

    student = {
        "Name"  : name,
        "Age"   : age,
        "Course": course
    }

    return student

def get_age():
    while True:
        try:
            age = int(input("Enter Student Age: "))

            if age == 0:
                print("You are Just Born")
            elif age < 0:
                print("Age can't be a Negative Number")
            elif age < 15:
                print("You are too YOUNG To be a Student")
            elif age > 25:
                print("You are too OLD To be a Student")
            else:
                break
        except ValueError:
            print("Please Enter an integer for Age")

    return age

def display_student(student):
    print()
    print("+----------------------------------+")
    print("|        STUDENT DETAILS           |")
    print("+----------------------------------+")

    print(f"| Name   : {student['Name']:<24}|")
    print(f"| Age    : {student['Age']:<24}|")
    print(f"| Course : {student['Course']:<24}|")

    print("+----------------------------------+")

def main():
    student = get_student_details()
    display_student(student)

if __name__ == "__main__":
    main()