class Bankaccount:
    def __init__(self,name_owner,balance):
        self.name_owner = name_owner
        self.balance = balance
        print(f"Initial balance : {self.balance}")
    def deposit_money(self,amount):
        self.balance += amount
        print(f"{self.name_owner} has deposited an amount of {amount} dollars")

    def withdraw_money(self,amount):
        if amount > self.balance:
           print(f"{self.name_owner} has insufficient funds")

        else:
            self.balance -= amount
            print(f"{self.name_owner} has withdrawn an amount of {amount}")

    def show_balance(self):
        print(f"{self.name_owner} has a balance of {self.balance}")

#Example/ Object creation
account1 = Bankaccount("John",500)
account1.deposit_money(100)
account1.withdraw_money(650)
account1.withdraw_money(100)
account1.show_balance()