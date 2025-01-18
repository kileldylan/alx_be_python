class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return self.account_balance
        else:
            print("Deposit amount must be positive.")
            return None

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        elif amount > 0:
            self.account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display(self):
        print(f"Current Balance: Ksh {self.account_balance:.2f}")
