#Create a BankAccount class with:
#- owner
#- balance
#- deposit(amount) → adds money
#- withdraw(amount) → removes money
#- display_balance() → shows current balance


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)


account = BankAccount("Rahul", 5000)

account.display_balance()

account.deposit(2000)
print("\nAfter depositing 2000:")
account.display_balance()

account.withdraw(1500)
print("\nAfter withdrawing 1500:")
account.display_balance()