from util import balance,transactions
def withdraw_money():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        transactions.append(f"Withdrawn ₹{amount}")
        print("Withdrawal successful")
    else:
        print("Insufficient balance")