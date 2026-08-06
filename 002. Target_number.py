numbers = [1,2,3,4,5,6,7,8,9]
target = 4
found = False

for index in range(len(numbers)):
    if target == numbers[index]:
        print(f"The number {target} found at index {index}")
        found = True
        break

if not found:
    print(f"The number {target} not found")