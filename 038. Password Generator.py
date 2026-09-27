# Password Generator

import random
import string

while True:
    try:
        length = int(input("Enter the Password Length: "))
        break

    except ValueError:
        print("Invalid Input")

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
special = string.punctuation

chars = uppercase + lowercase + numbers + special

password = ""

for i in range(length):
    password += random.choice(chars)

print()
print("PASSWORD GENERATOR")
print("------------------")
print(f"Password : {password}")