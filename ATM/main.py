from deposite_money import deposit_money
from  display_balance import display_balance
from statement import show_statement
from withdraw_money import withdraw_money

def menu():
    while True:
        print("\n---- ATM MENU ----")
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            show_statement()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice")
menu()