# Symbol Grid Program

while True:
    try:
        rows = int(input("Please enter a number of rows: "))
        break

    except ValueError:
        print("Please Enter a Valid Input")


while True:
    try:
        columns = int(input("Please enter a number of columns: "))
        break

    except ValueError:
        print("Please Enter a Valid Input")


symbol = input("Please enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()