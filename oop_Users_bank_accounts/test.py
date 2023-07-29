class User :
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bank_account = BankAccount (0.02,0)
    

    def make_deposit(self, amount):
        self.bank_account.deposit(amount)
        return self
    
    def display_balance(self):
        self.bank_account.display_account_info()
        return self
    

    def transfer_money(self,receiver, amount):
        if self.bank_account.check_withdraw(self.bank_account.balance, amount):
            self.bank_account.withdraw(amount)
            receiver.make_deposit(amount)
            print("OPERATION SUCCESS ! ")
            return self
        else:
            print("OPERATION FAILED! ")
            return self

john = User("John", 'john@email.com')
alice = User("Alice", 'alice@email.com')

print("--------------JOHN BALANCE v0----------------")
john.display_balance()
john.make_deposit(500)
print("--------------JOHN BALANCE V1----------------")
john.display_balance()
print("--------------ALICE BALANCE V0----------------")
alice.display_balance()
john.transfer_money(alice,100)
print("--------------ALICE BALANCE V1----------------")
alice.display_balance()
print("--------------JOHN BALANCE V2----------------")
john.display_balance()