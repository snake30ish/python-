class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f" your balance mr {self.account_holder} after the deposit {amount} is {self.balance} euro.")

    def withdraw(self, amount):
        if self.balance < amount:
            print("not enough credit.")
        else:
            self.balance -= amount
            print(f"transaction {amount} euro succefully. new balance: {self.balance} euro.")

    def display_balance(self):
        print(f"your balance is {self.balance} euro.")


lazaros=BankAccount("Lazaros", 100)
lazaros.deposit(3000)
print(lazaros.display_balance())
print(lazaros.withdraw(500))
print(lazaros.display_balance())
print(lazaros.deposit(500))
