class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False  # Return False instead of printing "Insufficient funds."

    def display_balance(self):
        # Use the expected "$" format
        print(f"Current Balance: ${self.account_balance:.2f}")
