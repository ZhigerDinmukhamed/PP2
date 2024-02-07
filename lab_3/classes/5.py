class Account:
    def __init__(var, owner, balance=0):
        var.owner = owner
        var.balance = balance

    def deposit(var, amount):
        var.balance += amount
        print("Deposit of {amount} accepted. New balance: {var.balance}")

    def withdraw(var, amount):
        if amount <= var.balance:
            var.balance -= amount
            print("Withdrawal of {amount} accepted. New balance: {var.balance}")
        else:
            print("Insufficient funds. Withdrawal rejected.")

account = Account("Zhiger", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(800)
account.deposit(300)
account.withdraw(1200)