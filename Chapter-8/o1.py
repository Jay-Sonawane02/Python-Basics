class Account:
    def __init__(self):
        self.accNo = int(input("Enter Acc No: "))
        self.balance = int(input("Enter Balance: "))
        
    def debit(self):
        amt = int(input("\nEnter amt to debit: "))
        self.balance -=amt
        self.getBalance()
    
    def credit(self):
        amt = int(input("\nEnter amount to credit: "))
        self.balance +=amt
        self.getBalance()
    
    def getBalance(self):
        print("Balance: ",self.balance)

a1 = Account()
a1.debit()
a1.credit()
a1.getBalance()
