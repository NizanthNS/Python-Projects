# Fibonacci series

while True:
    try:
        n = int(input("Enter the number of terms for Fibonacci series: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer")
    except ValueError:
        print("Invalid input! Please enter a positive integer.")

a = 0
b = 1

for i in range(n):
    print(a, end = " ")

    c = a + b
    a = b
    b = c