# Square Root Calculator

import math

while True:
    try:
        num = int(input("Enter a number to calculate its Square Root: "))

        if num < 0:
            print("Please Enter a Non-Negative Integer")
            continue

        break

    except ValueError:
        print("Please Enter an Integer")

x = math.sqrt(num)

print(f"The Square Root of {num} is {x:.2f}")