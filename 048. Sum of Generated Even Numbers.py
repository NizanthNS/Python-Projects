# Sum of Generated Odd Numbers

numbers = []
even_sum = 0

for i in range(1, 31):
    numbers.append(i)

for num in numbers:
    if num % 2 == 0:
        even_sum += num

print(even_sum, end = " ")