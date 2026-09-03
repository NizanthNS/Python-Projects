# Python Weight Converter

while True:
    try:
        weight = float(input("Enter your weight: "))
        break
    except ValueError:
        print("Please Enter a Valid Integer")

unit = input("Kilogram or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{weight}{unit} is not a valid unit")