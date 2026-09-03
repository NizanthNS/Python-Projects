# Python Compound Interest Calculator

principle = 0
rate = 0
time = 0


while True:
    try:
        principle = float(input("Enter the Principle Amount: "))
        if principle < 0:
            print("Principle cannot be less than zero.")
        else:
            break
    except ValueError:
        print("Please Enter a Valid Integer")

while True:
    try:
        rate = float(input("Enter the Rate of Interest: "))
        if rate < 0:
            print("Rate of Interest cannot be less than zero.")
        else:
            break
    except ValueError:
        print("Please Enter a Valid Integer")

while True:
    try:
        time = int(input("Enter the time In Years: "))
        if time < 0:
            print("Time cannot be less than zero.")
        else:
            break
    except ValueError:
        print("Please Enter a Valid Integer")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")