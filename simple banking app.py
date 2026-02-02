balance = 0

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited: ₹", amount)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn: ₹", amount)
    else:
        print("Insufficient Balance!")


def check_balance():
    print("Current Balance: ₹", balance)


while True:
    print("\n--- Banking Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = float(input("Enter deposit amount: "))
        deposit(amt)

    elif choice == 2:
        amt = float(input("Enter withdrawal amount: "))
        withdraw(amt)

    elif choice == 3:
        check_balance()

    elif choice == 4:
        print("Thank you for using the banking application!")
        break

    else:
        print("Invalid choice!")
