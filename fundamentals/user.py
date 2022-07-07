
from bankaccount import BankAccount


class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        # this is adding another class into this one and gives us BankAccount functionality when we activate an account
        self.account = BankAccount()


    # the property decorator turns a method with no parameters into a attribute
    @property
    def display_info(self):
        print(f"First Name {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nRewards Member? {self.is_rewards_member}\nGold Card Points: {self.gold_card_points}")


    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        self.gold_card_points -= amount


    
    # these are instances of the Bankaccount class
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdraw(self,amount):
        self.account.withdraw(amount)

    # the property decorator turns a method with no parameters into a attribute
    @property
    def display_user_balance(self):
        self.account.display_account_info()



johnny = User('Johnny', 'Cash', 'jcash@yahoo.com', '50')
# johnny.display_info
# johnny.make_deposit(5000)
# johnny.make_withdraw(2000)
# johnny.display_user_balance
johnny.display_user_balance
johnny.enroll() 
johnny.display_info
