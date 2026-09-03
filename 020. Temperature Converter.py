# Temperature Converter

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

while True:
    try:
        temp = float(input("Enter the Temperature: "))
        break
    except ValueError:
        print("Please Enter a Valid Integer")

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"The Temperature is {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The Temperature in Celsius is: {temp}°C") # 0176 or 0178
else:
    print(f"{unit} is not a valid unit")