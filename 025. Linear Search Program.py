# Linear Search Program

numbers = []

for i in range(6, 10):
    numbers.append(i)

while True:
    try:
        target = int(input("Enter the number to Search: "))
        break

    except ValueError:
        print("INVALI INPUT")

found = False



for index in range(len(numbers)):
    if target == numbers[index]:
        print(f"The number {target} found at the Index {index}")
        found = True
        break

if not found:
    print(f"The number {target} not found")
