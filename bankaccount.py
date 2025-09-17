class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        elif amount > 0:
            self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    account = BankAccount(100)
    print(f"Initial balance: {account.get_balance()}")
    account.deposit(50)
    print(f"After deposit: {account.get_balance()}")
    result = account.withdraw(30)
    print(f"After withdrawal: {account.get_balance()}")
    result = account.withdraw(200)
    print(f"Withdrawal result: {result}")
    print(f"Final balance: {account.get_balance()}")