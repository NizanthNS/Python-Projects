# Concession Stand Program
# Dictionary {key : value}

menu = {"pizza" : 5.00,
        "burgers" : 3.50,
        "fries" : 2.00,
        "nachos" : 1.50,
        "soda" : 1.00,
        "cheese" : 1.00,
        "lemonade" : 1.50,
        "puffs" : 2.50,
        "sandwich" : 3.00,
        "popcorn" : 7.00}

cart = []
total = 0.0

print("----------MENU-------------")
for key, value in menu.items():
    print(f"{key:10} : {value:.2f}")
print("---------------------------")

while True:
    food = input("Select a food item From the Menu (Q to Quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("That item is not on the menu.")

print("------ YOUR ORDER ----------")
for food in cart:
    total += menu.get(food)
    print(f"{food:10} : {menu.get(food):.2f}")
print("----------------------------")
print(f"Total : {total:.2f}")
print("----------------------------")