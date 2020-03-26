import threading


class BankAccount(object):
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.balance = 0
        self.is_open = False

    def IsAccountOpen(func):
        def wrapper(self, *args):
            if not self.is_open:
                raise ValueError("Account is closed")
            return func(self, *args)

        return wrapper

    @IsAccountOpen
    def get_balance(self):
        return self.balance

    def open(self) -> None:
        if not self.is_open:
            self.is_open = True
        else:
            raise ValueError("Account is already open")

    @IsAccountOpen
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("deposit amount cannot be negative")
        self.balance = self.balance + amount

    @IsAccountOpen
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("withdraw amount cannot be negative")
        if amount > self.balance:
            raise ValueError("withdraw amount cannot be bigger than balance")
        self.balance = self.balance - amount

    @IsAccountOpen
    def close(self):
        self.is_open = False
        self.balance = 0
