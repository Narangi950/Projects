from util import balance,transactions
def show_statement():
    print("\nTransaction History:")
    if len(transactions) == 0:
        print("No transactions yet")
    else:
        for t in transactions:
            print(t)