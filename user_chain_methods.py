#Python User assignment w/ Chaining Methods
class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

#USERS
logan = User("Logan Awesome's", "slayincode@gmail.com")
jac = User("Jac Gunna", "gunnajacuup@gmail.com")
dave = User("Dave Naugler", "davenaugler@gmail.com")
anna = User("Anna Kendrick", "annagunnabenicenow@gmail.com")

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
logan.make_deposit(1000).make_deposit(500).make_deposit(100).display_user_balance()
# print(logan.account_balance)
#Account Balance = 1600

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
jac.make_deposit(1000).make_deposit(2000).make_withdrawal(50).make_withdrawal(50).display_user_balance()
#Account Balance = 2900

dave.make_deposit(1000).make_withdrawal(200).make_withdrawal(500).make_withdrawal(500).display_user_balance()
#Account Balance = -200

logan.make_deposit(1000).display_user_balance()

jac.transfer_money(logan, 100).display_user_balance()
logan.display_user_balance()
