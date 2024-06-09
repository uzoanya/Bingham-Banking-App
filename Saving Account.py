class SavingsAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def deposit(self, amount):
        super().deposit(amount)
        interest = 0.005 * amount
        self._balance += interest
        print(f"Added interest {interest}. New balance: {self._balance}")
    def withdraw(self, amount):
        if amount > 700000:
            print("Withdrawal limit exceeded")
        else:
            super().withdraw(amount)
# Example Usage
savings = SavingsAccount("John Doe", 1000)
savings.deposit(1000)
savings.withdraw(500)

