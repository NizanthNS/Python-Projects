# Diamond Program

while True:
    try:
        rows = int(input("Enter number of rows: "))
        break
    except ValueError:
        print("Please Enter an Integer")

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1

    print(" " * spaces + "*" * stars)

for i in range(2, rows + 1):
    spaces2 = i - 1
    stars2 = 2 * (rows - i + 1) - 1

    print(" " * spaces2 + "*" * stars2)

