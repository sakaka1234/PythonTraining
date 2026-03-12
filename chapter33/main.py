def withdraw(balance,amount):
    if amount > balance:
        raise Exception("Not enough money")
    return balance - amount

try:
    withdraw(100,200)
except Exception as e:
    print(e)