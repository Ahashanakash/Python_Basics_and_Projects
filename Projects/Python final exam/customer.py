import random
from user import User 

class Customer(User):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.balance = 0
        self.history = []
        self.loan_count = 0
        self.loan_amount = 0
        self.account_number = random.randint(101, 999)

    def deposite(self, bank, amount):
        self.balance += amount
        bank.balance += amount
        self.history.append(f"Deposite amount = {amount}")
        print(f"Tk {amount} deposite successful.\nNew balance = {self.balance}")

    def withdraw(self, bank, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
            return
        if bank.balance < amount:
            print(f"{bank.name} is bankrupt")
            if bank.balance <= 0:
                bank.balance = 0
            return
        else:
            self.balance -= amount
            bank.balance -= amount
            self.history.append(f"Withdraw amount = {amount} tk")
            print(
                f"Tk {amount} withdrawal successful.\nNew balance = {self.balance} tk"
            )

    def check_balance(self):
        print("Balance = ", self.balance, "tk")

    def transaction_history(self):
        print("Transaction history")
        for hist in self.history:
            print(hist)

    def take_loan(self, bank):
        if bank.loan_feature == False:
            print("Loan feature is off")
            return
        if self.loan_count == 2:
            print("Loan taking limit exceeded")
            return
        else:
            amount = int(input("Loan amount = "))
            if bank.balance < amount:
                print("Loan amount is too high.")
                return
            bank.balance -= amount
            bank.loan += amount
            self.loan_amount += amount
            self.history.append(f"Loan {amount} tk has been taken from {bank.name}.")
            print(f"Loan {amount} tk taken from {bank.name}.")
            self.loan_count += 1
            

    def view_ac_no(self):
        print("Account number = ", self.account_number)

    def transfer_amount(self, bank, account_number, amount):
        if amount > self.balance:
            print("No sufficient balance")
        else:
            acnt = bank.find_account(account_number)
            if acnt:
                acnt.balance += amount
                self.balance -= amount
                self.history.append(
                    f"Transfered {amount} tk to account no {account_number}"
                )
                acnt.history.append(
                    f"Recieved {amount} tk from account no {self.account_number}"
                )
                print(f"{amount}tk transfered to account no {account_number}")
            else:
                print("Account does not exist.")