


class BankAccount:

    def __init__(self, balance=0, interest_rate=.01) -> None:
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1- self.interest_rate)
            return self


# account1 = BankAccount(5000, .02)
# account1.deposit(100).deposit(100).deposit(100).withdraw(100).display_account_info()
# account2 = BankAccount(1000)
# account2.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()
