# Sum of Fibonacci series

while True:
    try:
        n = int(input("Enter the number of terms for Fibonacci series to SUM it: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer")
    except ValueError:
        print("Invalid input! Please enter a positive integer.")

a = 0
b = 1
sum_ = 0

for i in range(n):
    print(a, end = " ")

    sum_ = sum_ + a

    c = a + b
    a = b
    b = c

print()
print("Sum is: ", sum_)