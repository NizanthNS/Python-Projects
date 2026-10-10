# Sum of Generated Odd Numbers

numbers = []
odd_sum = 0

for i in range(1, 21):
    numbers.append(i)

for num in numbers:
    if num % 2 != 0:
        odd_sum += num

print(odd_sum)