# Python Calculator

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

def main():
    while True:
        try:
            num1 = int(input("Enter the 1st Number: "))
            num2 = int(input("Enter the 2nd Number: "))
            break
        except ValueError:
            print("Please enter a valid number")

    add = addition(num1, num2)
    sub = subtraction(num1, num2)
    mul = multiplication(num1, num2)
    dvr = division(num1, num2)

    print()
    print("-----------------------")
    print("      CALCULATOR       ")
    print("-----------------------")
    print(f"Addition       : {add}")
    print(f"Subtraction    : {sub}")
    print(f"Multiplication : {mul}")
    print(f"Division       : {dvr}")
    print("-----------------------")

if __name__ == "__main__":
    main()
