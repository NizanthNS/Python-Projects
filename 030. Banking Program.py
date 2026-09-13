# Python Banking Program

def show_balance(balance):
    print(f"Current Balance: ${balance:.2f}")

def deposit():
    while True:
        try:
            amount = float(input("Enter the Amount to Deposit: "))
            if amount <= 0:
                print("That's Not a Valid Amount")
                return 0
            else:
                return amount

        except ValueError:
            print("Please Enter a Valid Input")

def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter the Amount to Withdraw: "))

            if amount > balance:
                print("Insufficient funds")
                return 0
            elif amount <= 0:
                print("That's Not a Valid Amount")
                return 0
            else:
                return amount

        except ValueError:
            print("Please Enter a Valid Input")

def main():
    balance = 0
    is_running = True

    while is_running:
        try:
            print("Welcome to Banking Program")
            print("1. Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice (1 - 4): "))

            if choice == 1:
                show_balance(balance)
            elif choice == 2:
                balance += deposit()
            elif choice == 3:
                balance -= withdraw(balance)
            elif choice == 4:
                is_running = False
            else:
                print("That is not a valid choice, Please enter your choice (1 - 4): ")

        except ValueError:
            print("Please Enter a Valid Input")

    print("Thank you! Have a nice day!")

main()