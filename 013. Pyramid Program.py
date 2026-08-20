rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1

    # spaces = i - 1
    # stars = 2 * (rows - i + 1) - 1    -- Inverted Pyramid

    print(" " * spaces + "*" * stars)