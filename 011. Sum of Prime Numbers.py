# Sum of Prime Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_ = 0

for n in numbers:
    if n < 2:
        continue

    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        sum_ += n

print(sum_)
