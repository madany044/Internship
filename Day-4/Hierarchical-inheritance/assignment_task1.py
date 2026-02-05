class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print("Interest Added:", interest)


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Amount Withdrawn with Overdraft:", amount)
        else:
            print("Overdraft Limit Exceeded")


savings = SavingsAccount("Madan", 10000, 5)
savings.deposit(2000)
savings.add_interest()
savings.withdraw(3000)
savings.display_balance()

print()

current = CurrentAccount("Rahul", 5000, 2000)
current.deposit(1000)
current.withdraw_with_overdraft(6500)
current.display_balance()
