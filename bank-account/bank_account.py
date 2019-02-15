"""Implement a simple class to manage a bank account."""
from threading import Lock

LOCK = Lock()


class BankAccount(object):
    """Implement a simple class to manage a bank account."""

    def __init__(self):
        self.balance = 0
        self.is_open = False

    def is_already_open(func):
        def wrapper(self, *args):
            if not self.is_open:
                raise ValueError("Account is closed")
            return func(self, *args)
        return wrapper

    @is_already_open
    def get_balance(self):
        """Get account balance."""
        return self.balance

    def open(self):
        """Open an account."""
        if not self.is_open:
            self.is_open = True
        else:
            raise ValueError("Account is already open")

    @is_already_open
    def deposit(self, amount):
        """Deposit money."""
        if amount < 0:
            raise ValueError("deposit amount cannot be negative")
        self.balance = self.balance + amount

    @is_already_open
    def withdraw(self, amount):
        """Withdraw money."""
        if amount < 0:
            raise ValueError("withdraw amount cannot be negative")
        if amount > self.balance:
            raise ValueError("withdraw amount cannot be bigger than balance")
        self.balance = self.balance - amount

    @is_already_open
    def close(self):
        """Close an account."""
        self.is_open = False
        self.balance = 0
