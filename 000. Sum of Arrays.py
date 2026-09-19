# Sum of Arrays

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_ = 0

for num in numbers:
    sum_ += num

print("The Sum of Numbers is", sum_)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(numbers))

# Running Sum

sum_ = 0

for num in range(1, 10):
    sum_ += num

print(sum_)

# Running Sum - 2

numbers = []

for i in range(1, 5):
    numbers.append(i)

sum_ = 0

for num in numbers:
    sum_ += num

print(sum_)
