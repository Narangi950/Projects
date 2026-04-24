from util import balance,transactions

def deposit_money():   
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    transactions.append(f"Deposited ₹{amount}")
    print("Deposit successful")