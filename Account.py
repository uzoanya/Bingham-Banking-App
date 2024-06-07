class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def desposit(self, amount):
        self.balance += amount
        self.balance += amount
        print("deposit{amount}.New balance:{'self.balance'}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdraw{amount}.New balance:{self.balance}")
        else:
            print("insufficient balance")


    def getbalance(self):
        return self.balance

    def getowner(self):
        return self.owner

