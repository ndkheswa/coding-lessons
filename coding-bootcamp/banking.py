#!/usr/local/bin/python3

class Account:
    
    AMOUNT_MIN = 150
    
    def __init__(self, balance, account_type):
        self.balance = balance
        self.account_type = account_type
        if self.balance >= self.AMOUNT_MIN:
            self.active = True
            return print(f'A new account has been created. Your current balance is {self.balance}.')        
        else:
            self.active = False
            return print(f'The balance is lower than the minimum amount required. Please deposit an amount greater or equal to {self.AMOUNT_MIN}')
    
    def deposit(self, amount):
        self.balance += amount
        if self.balance >= self.AMOUNT_MIN:
            self.active = True
            return print(f'You\'ve deposited {amount}. Your new balance is {self.balance}')
    
    def withdraw(self, amount):
        if amount > self.balance:
            return print(f'The amount requested, {self.balance} is greated than the available balance!')
        else:
            self.balance -= amount
        return print(f'You\'ve withdrawn {amount} from your {self.account_type} account. Your new balance is {self.balance}')
    
A = Account(140, "checque")

A.deposit(500)

A.withdraw(150)

