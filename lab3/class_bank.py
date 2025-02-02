class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: " + str(amount))
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: " + str(amount))
        else: 
            print("Not enough money on your bank account.")
    def left_money(self):
        print("Balance: " + str(self.balance))

owner = input("Name: ")
balance = int(input("Balance: "))
acc = Bank_account(owner, balance)
acc.deposit(int(input("Put: ")))
acc.left_money()
acc.withdraw(int(input("Take: ")))
acc.left_money()

