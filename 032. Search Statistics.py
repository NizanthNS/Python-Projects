# Advanced Linear Search with Statistics

numbers = [12, 5, 18, 7, 18, 3, 18, 10]
target = 18

total = 0
count = 0
first_index = None
last_index = None
highest_match = None
lowest_match = None

for index in range(len(numbers)):
    if target == numbers[index]:
        count += 1
        total += numbers[index]

        if first_index is None:
            first_index = index

        last_index = index

        if highest_match is None:
            highest_match = numbers[index]
            lowest_match = numbers[index]

        if numbers[index] > highest_match:
            highest_match = numbers[index]

        if numbers[index] < lowest_match:
            lowest_match = numbers[index]

if count > 0:
    average = total / count
else:
    average = 0

print(f"Number of occurrences  : {count}")
print(f"First occurrence       : index {first_index}")
print(f"Last occurrence        : index {last_index}")
print(f"Sum of matching values : {total}")
print(f"Average                : {average}")
print(f"Highest match          : {highest_match}")
print(f"Lowest match           : {lowest_match}")