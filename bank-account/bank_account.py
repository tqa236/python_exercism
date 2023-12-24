import threading


class BankAccount(object):
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.balance = 0
        self.is_open = False

    def IsAccountOpen(func):
        def wrapper(self, *args):
            if not self.is_open:
                raise ValueError("account not open")
            return func(self, *args)

        return wrapper

    @IsAccountOpen
    def get_balance(self):
        self.lock.acquire()
        return self.balance

    def open(self) -> None:
        if not self.is_open:
            self.is_open = True
        else:
            raise ValueError("account already open")

    @IsAccountOpen
    def deposit(self, amount):
        self.lock.acquire()
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        self.balance = self.balance + amount
        self.lock.release()

    @IsAccountOpen
    def withdraw(self, amount):
        self.lock.acquire()
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("amount must be less than balance")
        self.balance = self.balance - amount
        self.lock.release()

    @IsAccountOpen
    def close(self):
        self.is_open = False
        self.balance = 0
