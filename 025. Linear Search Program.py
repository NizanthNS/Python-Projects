# Linear Search Program

numbers = []

for i in range(0, 21):
    numbers.append(i)

target = 15
found = False

for index in range(len(numbers)):
    if target == numbers[index]:
        print(f"The number {target} was found at index {index}.")
        found = True
        break

if not found:
    print(f"The number {target} was not found in the list.")