# Generate Prime Numbers

print("Prime Numbers : ", end = " ")

for n in range(1,101):

    if n < 2:
        continue

    is_prime = True

    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, end = " | ")