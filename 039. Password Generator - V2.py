# Password Generator -- Version 2

import random
import string

def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(special)
    ]

    characters = uppercase + lowercase + numbers + special

    for _ in range(length - 4):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)

def main():
    print()
    print("╔══════════════════════════════════════╗")
    print("║         PASSWORD GENERATOR           ║")
    print("╚══════════════════════════════════════╝")
    print()

    while True:
        try:
            length = int(input("Enter Password Length (Minimum 4 Characters): "))

            if length < 4:
                print("Invalid Length. Please Enter 4 or More.")
                continue

            break

        except ValueError:
            print("Invalid Input. Please Enter a Whole Number.")

    password = generate_password(length)

    print()
    print("========================================")
    print("          PASSWORD GENERATED")
    print("========================================")
    print()
    print(f"Password : {password}")
    print(f"Length   : {length}")
    print()
    print("----------------------------------------")
    print("Password Generation Complete.")
    print("========================================")
    print()

if __name__ == "__main__":
    main()