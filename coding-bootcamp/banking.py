class Account:
    balance = 0
    active = False
    account_type = ""
    account_number = 0000000
    def deposit(self, amount, acc_type):
        self.balance += amount
        self.account_type = acc_type
        return self.balance
    

        
    
A = Account()
A.deposit(100, "checque")
print(f'The balance is {A.balance}')

A.withdraw(25, "checque")
print(f'Your remaining balance is {A.balance}')

