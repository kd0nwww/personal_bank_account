from bank import Amount, PersonalAccount
import os

# Testing Amount class
amount = Amount(333.0, "11-02-2025 12:28:44", "DEPOSIT")
print(str(amount))

# Testing PersonalAccount class
number = int(input("Enter your account number: "))
holder = input("Enter your name: ")

acc = PersonalAccount(number, holder)

os.system("cls")

while True:

    os.system("cls")

    print("------------------------------MENU------------------------------")
    print("1 - Deposit                            6 - Change account number")
    print("2 - Withdrawal                         7 - Show holder's name")
    print("3 - Show history of transactions       8 - Change holder's name")
    print("4 - Show balance                       9 - Get info about account")
    print("5 - Show account number                0 - Exit")
    print()

    choice = int(input("Choose one option(1-9): "))

    os.system("cls")

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        acc.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        acc.withdraw(amount)

    elif choice == 3:
        acc.print_transaction_history()
        input()

    elif choice == 4:
        print(f"Your current balance is: {acc.get_balance()}")
        input()

    elif choice == 5:
        print(f"Your account number: {acc.get_account_number()}")
        input()

    elif choice == 6:
        new_acc_number = int(input("Enter new account number: "))
        acc.set_account_number(new_acc_number)

    elif choice == 7:
        print(f"Holder's name is: {acc.get_account_holder()}")
        input()

    elif choice == 8:
        new_acc_holder = input("Enter new account holder: ")
        acc.set_account_holder(new_acc_holder)

    elif choice == 9:
        print(str(acc))
        input()

    elif choice == 0:
        break

    else:
        print("Invalid Input")
        input()