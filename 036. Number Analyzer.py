# Number Analyzer

numbers = []
total = 0
highest_number = None
lowest_number = None
even_count = 0
odd_count = 0

for n in range(1,6):

    while True:
        try:
            number = int(input(f"Enter the Number {n}: "))
            numbers.append(number)
            break

        except ValueError:
            print("Please Enter an integer, It's a Number Analyzer Program")

for num in numbers:
    total += num

if len(numbers) > 0:
    average = total / len(numbers)
else:
    average = 0

for index in range(len(numbers)):
    if highest_number is None:
        highest_number = numbers[index]
        lowest_number = numbers[index]

    if numbers[index] > highest_number:
        highest_number = numbers[index]

    if numbers[index] < lowest_number:
        lowest_number = numbers[index]

for num in numbers:
    if num % 2 == 0:
        even_count += 1

for num in numbers:
    if num % 2 != 0:
        odd_count += 1

print()
print("         ANALYSIS RESULTS")
print("----------------------------------------")
print(f"        Total        : {total}")
print(f"        Average      : {average:.2f}")
print(f"        Highest      : {highest_number}")
print(f"        Lowest       : {lowest_number}")
print(f"        Even Numbers : {even_count}")
print(f"        Odd Numbers  : {odd_count}")
print("----------------------------------------")
print("         Analysis Complete")
print()
