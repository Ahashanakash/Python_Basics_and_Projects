from user import User

class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def delete_user_account(self, bank, account_number):
        bank.delete_account(account_number)

    def show_customer_list(self, bank):
        bank.show_list()

    def check_balance(self, bank):
        bank.check_bank_balance()

    def check_loan_ammount(self, bank):
        bank.check_loan_amount()

    def loan_feature(self, bank, on_off):
        bank.set_loan_feature(on_off)