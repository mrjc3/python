from curses import A_ALTCHARSET


class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


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


johnny = User('johhny', 'cash', 'jcash@gmail.com', '33')

johnny.enroll()
johnny.display_info()
johnny.spend_points(12)
johnny.enroll()
johnny.display_info()
