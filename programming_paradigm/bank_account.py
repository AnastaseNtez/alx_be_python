# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with optional initial balance (default is 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient. Returns True/False."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
