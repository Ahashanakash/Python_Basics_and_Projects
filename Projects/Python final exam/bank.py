class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.customer_list = []
        self.loan = 0
        self.loan_feature = 1

    def find_account(self, account_number):
        for acnt in self.customer_list:
            if account_number == acnt.account_number:
                return acnt
            
    def add_customer(self, customer):
        self.customer_list.append(customer)

    def delete_account(self, account_number):
        acnt = self.find_account(account_number)
        if acnt:
            self.customer_list.remove(acnt)
            print(f"Account number {account_number} has been deleted")
        else:
            print("Account does not exist")

    def show_list(self):
        if len(self.customer_list) == 0:
            print("Customer list is empty.")
            return
        print("Customer details " + "-" * 20)
        print(
            f"{'Customer name':<20} {'Account type' :<20} {'account number':<20} {'Balance':<20}"
        )
        for customer in self.customer_list:
            print(
                f"{customer.name:<20} {customer.account_type :<20} {customer.account_number:<20} {customer.balance:<20}"
            )

    def check_bank_balance(self):
        print(f"{self.name}'s available balance = ", self.balance)

    def check_loan_amount(self):
        print("Bank loan amount = ", self.loan)

    def set_loan_feature(self, turn):
        self.loan_feature = turn
        if turn == 0:
            print("Loan feature has been turned off")
        elif turn == 1:
            print("Loan feature has been turned on")
        else:
            print("Invalid command")