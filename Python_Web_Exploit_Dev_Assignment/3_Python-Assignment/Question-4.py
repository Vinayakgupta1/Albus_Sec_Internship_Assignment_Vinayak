# Create a Python class to represent a bank account with methods for deposit, withdrawal, and checking the balance.

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return self.balance
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance


account = BankAccount()
print("Deposit:- ", account.deposit(100))  
print("Withdraw:- ", account.withdraw(50))  
print("Balance :- ", account.check_balance())  