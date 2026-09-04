# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    try:
        food = input("Enter the food that you want to buy (q to Quit): ")
        if food.lower() == "q":
            break
        else:
            price = float(input(f"Enter the price of a {food} that you want to buy: $"))
            foods.append(food)
            prices.append(price)
    except ValueError:
        print("Please Enter a Valid Input")

print("----- YOUR CART -----")

for food in foods:
    print(food, end = " ")

for price in prices:
    total += price

print()
print(f"Total Price is: {total}$")