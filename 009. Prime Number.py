# Prime Number

while True:
    try:
        n = int(input("Enter a number: "))

        if n > 0:
            break
        else:
            print("Enter a positive integer")

    except ValueError:
        print("Invalid input, Please enter a positive integer")

if n < 2:
    print(f"{n} is not a prime number")
else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")