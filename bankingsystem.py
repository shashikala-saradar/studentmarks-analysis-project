class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"current balance is {self.balance}")
        else:
            print("invalid amount")
    def withdraw(self,amou):
        if amou>self.balance:
            print("insufficient")
        else:
            self.balance-=amou
            print(f"withdrawn money is {self.balance}")



a=BankAccount(101,"shashi",10000)
a.deposit(100)
a.withdraw(500)

