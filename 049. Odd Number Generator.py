# Odd Number Generator

numbers = []

for i in range(1, 101):
    numbers.append(i)

for num in numbers:
    if num % 2 != 0:
        print(num, end = " ")