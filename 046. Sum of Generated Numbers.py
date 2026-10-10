# Sum of Generated Numbers

numbers = []
sum_ = 0

for i in range(1, 21):
    numbers.append(i)

for num in numbers:
    sum_ += num

print(sum_)