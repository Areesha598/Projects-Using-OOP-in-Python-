
print("....BANK ACCOUNT....".center(100))

class BankAccount:
    def __init__(self,name,customerId,balance):
        self.name = name
        self.customerId = customerId
        self.balance = balance
    def display(self):
        print(f"{self.name} has customer ID {self.customerId} having balance {self.balance} Rupees.")

    def Tbalance(self):
        print(f"Your Balance is {self.balance}")

    def deposit(self,amount):
        if amount < 0:
            print("Invalid Amount.")
        else:
            self.balance += amount
            print(f"Total Amount is {self.balance} Rupees.")
      

    def withdraw(self,amount):
        if amount > self.balance:
            print("Error Enter Valid Amount.")
        else:
            self.balance -= amount
            print(f"You withdraw {amount} Rupees.Your current balance is {self.balance} Rupees.")


class SavingAccount(BankAccount):
    def __init__(self,amount,percent,name, customerId, balance):
        super().__init__(name, customerId, balance)
        self.amount = amount
        self.percent = percent 
    
    def calcInterest(self):
        interest = (self.amount * self.percent)/100
        print(f"You should give interest of {self.percent}% which is equal to {interest} Rupees.")
        

class CurrentAccount(BankAccount):
    def __init__(self, name, customerId, balance):
       super().__init__(name, customerId, balance)









bnk = BankAccount("ABC",1122,1000)
bnk.display()
bnk.Tbalance()
bnk.deposit(200)
bnk.Tbalance()
sve = SavingAccount(1000,5,"ABC",1122,1000)
sve.calcInterest()
