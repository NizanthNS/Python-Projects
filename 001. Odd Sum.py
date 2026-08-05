numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_sum = 0

for num in numbers:
    if num % 2 != 0:
        odd_sum += num

print("The Sum of odd number is",odd_sum)