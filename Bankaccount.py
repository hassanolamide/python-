class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
            self.balance = self.balance + amount
    def subtract(self, amount):
        if amount > self.balance:
              print("Insufficience balance")
        else:
            self.balance = self.balance - amount
    def check_balance(self):
        print(f"Your remaining balance is ₦{self.balance:,}")

        