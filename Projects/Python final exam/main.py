from user import User
from customer import Customer
from admin import Admin
from bank import Bank

bank = Bank("Bangladesh Bank", 100)

while 1:
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter choice = "))

    if choice == 1:
        name = input("Name - ")
        email = input("Email - ")
        address = input("Address - ")
        at = input("Account Type - ")

        customer = Customer(name, email, address, at)
        bank.add_customer(customer)
        print(f"Welcome {customer.name} (Customer)!")
        while 1:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. History")
            print("5. Loan")
            print("6. Transfer balance")
            print("7. View account number")
            print("8. Exit")

            option = int(input("Enter option = "))

            if option == 1:
                amount = int(input("Enter deposite amount = "))
                if amount < 1:
                    print("Invalid amount.")
                else:
                    customer.deposite(bank, amount=amount)

            elif option == 2:
                amount = int(input("Enter withdraw amount = "))
                if amount < 1:
                    print("Invalid amount.")
                else:
                    customer.withdraw(bank, amount=amount)

            elif option == 3:
                customer.check_balance()

            elif option == 4:
                customer.transaction_history()

            elif option == 5:

                customer.take_loan(bank)

            elif option == 6:
                ac_unm = int(input("Account number = "))
                amount = int(input("Amount = "))
                if amount < 1:
                    print("Invalid amount.")
                else:
                    customer.transfer_amount(bank, ac_unm, amount)

            elif option == 7:
                customer.view_ac_no()

            elif option == 8:
                print("Exit")
                break

            else:
                print("Invalid comman")

    elif choice == 2:
        name = input("Name - ")
        email = input("Email - ")
        address = input("Address - ")

        admin = Admin(name, email, address)
        print(f"Welcome {admin.name} (Admin)!")
        while 1:
            print("1. Delete customer")
            print("2. List of customers")
            print(f"3. {bank.name}'s available balance")
            print(f"4. {bank.name}'s total loan amount")
            print("5. Loan feature")
            print("6. Exit")

            option = int(input("Enter option = "))

            if option == 1:
                ac_num = int(input("Enter account number = "))
                admin.delete_user_account(bank, ac_num)

            elif option == 2:
                admin.show_customer_list(bank)

            elif option == 3:
                admin.check_balance(bank)

            elif option == 4:
                admin.check_loan_ammount(bank)

            elif option == 5:
                on_off = int(input("Enter option (0=off or 1=on)  = "))
                admin.loan_feature(bank, on_off)

            elif option == 6:
                print("Exit.")
                break
            else:
                print("Invalid command.")

    elif choice == 3:
        print("Exit..")
        break
    else:
        print("Invalid Command")
