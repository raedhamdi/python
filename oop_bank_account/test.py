class BankAccount :

   
    def __init__(self, int_rate=0.025, balance=0):
       
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"[DEPOSIT] You added {amount}$ to you Bank Account.You balance is equal to {self.balance}$.")
        return self
    

    def withdraw(self, amount):
        return self


    def display_account_info(self):
       print(f"-----ACCOUNT INFO----\nINTEREST RATE : {self.int_rate}\nBALANCE : {self.balance}")
       return self
    
    def __repr__(self):
        return f"-----ACCOUNT INFO----\nINTEREST RATE : {self.int_rate}\nBALANCE : {self.balance}"
    

    def yield_interest(self):
        return self


default_account = BankAccount()

custom_account = BankAccount(0.2,1000)


print(custom_account)
custom_account.yield_interest()
print(custom_account)