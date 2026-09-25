# Student Score Analyzer

marks = []
names = []
total = 0
highest_scorer = None
lowest_scorer = None
highest_mark = None
lowest_mark = None
passed_count = 0
failed_count = 0

for i in range(1, 6):
    while True:
        try:
            name = input(f"Enter Student {i} Name: ")
            names.append(name)

            mark = int(input(f"Enter {name}'s Mark: "))
            marks.append(mark)

            break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

for num in marks:
    total += num

average_mark = total / len(marks)

for index in range(len(marks)):
    if highest_mark is None:
        highest_mark = marks[index]
        lowest_mark = marks[index]
        highest_scorer = names[index]
        lowest_scorer = names[index]

    if marks[index] > highest_mark:
        highest_mark = marks[index]
        highest_scorer = names[index]

    if marks[index] < lowest_mark:
        lowest_mark = marks[index]
        lowest_scorer = names[index]

for mark in marks:
    if mark >= 40:
        passed_count += 1

for mark in marks:
    if mark < 40:
        failed_count += 1

print()
print("========================================")
print("        STUDENT SCORE ANALYZER")
print("========================================")
print()
print(f"Highest Scorer : {highest_scorer} - {highest_mark}")
print(f"Lowest Scorer  : {lowest_scorer} - {lowest_mark}")
print(f"Average Mark   : {average_mark:.2f}")
print(f"Passed         : {passed_count}")
print(f"Failed         : {failed_count}")
print()
print("----------------------------------------")
print("Analysis Complete")
print("========================================")