# Even Number Generator

numbers = []

for i in range(10, 29):
    numbers.append(i)

for num in numbers:
    if num % 2 == 0:
        print(num, end = " ")