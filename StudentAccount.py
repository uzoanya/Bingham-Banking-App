
class StudentAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def deposit(self, amount):
        if amount > 50000:
            print("Deposit limit exceeded")
        else:
            super().deposit(amount)
    def withdraw(self, amount):
        if amount > 2000:
            print("Withdrawal limit exceeded")
        else:
            super().withdraw(amount)


