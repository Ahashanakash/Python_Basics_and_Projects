from restaurant import Restaurant
from user import User
from employee import Employee
from admin import Admin
from customer import Customer
from menu import Menu
from order import Order
from items import Items


shah_amanot_hotel = Restaurant("Shah Amanot Hotel")

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter choice - "))

    if choice == 1:
        name = input("Enter name - ")
        phone = input("Enter phone - ")
        email = input("Enter email - ")
        address = input("Enter address - ")

        print(f"Welcome - {name} (Customer)")
        customer = Customer(name, phone, email, address)
        while True:
            print("1. View Menu")
            print("2. Add item to cart")
            print("3. Remove item from cart")
            print("4. View cart")
            print("5. Paybill")
            print("6. Exit")

            option = int(input("Enter option - "))

            if option == 1:
                customer.show_menu(shah_amanot_hotel)
            elif option == 2:
                p_name = input("Enter product name - ")
                p_quantity = int(input("Enter quantity - "))
                customer.add_item_to_cart(
                    shah_amanot_hotel, product_name=p_name, quantity=p_quantity
                )
            elif option == 3:
                p_nam = input("Enter product name - ")
                customer.remove_from_cart(shah_amanot_hotel, product_name=p_nam)
            elif option == 4:
                customer.view_cart()
            elif option == 5:
                customer.paybill()
            elif option == 6:
                break

    elif choice == 2:
        name = input("Enter name - ")
        phone = input("Enter phone - ")
        email = input("Enter email - ")
        address = input("Enter address - ")

        admin = Admin(name, phone, email, address)
        print(f"Welcome - {name} (Admin)")
        while True:
            print("1. Add new item")
            print("2. Add employee")
            print("3. View employee")
            print("4. View item")
            print("5. Delete item")
            print("6. exit")

            option = int(input("\nEnter option - "))

            if option == 1:
                p_name = input("Product name - ")
                quantity = int(input("Quantity - "))
                price = int(input("price - "))
                item = Items(product_name=p_name, quantity=quantity, price=price)
                admin.add_items(shah_amanot_hotel, item)

            elif option == 2:
                nam = input(" Employee's name - ")
                phon = input(" Employee's phone number - ")
                email = input(" Employee's email - ")
                adress = input(" Employee's address - ")
                age = int(input(" Employee's age - "))
                designation = input(" Employee's designation - ")
                salary = int(input(" Employee's salary - "))

                employee = Employee(
                    name=nam,
                    phone=phon,
                    email=email,
                    address=adress,
                    age=age,
                    designation=designation,
                    salary=salary,
                )

                admin.add_employees(shah_amanot_hotel, employee=employee)

            elif option == 3:
                admin.view_employees(shah_amanot_hotel)

            elif option == 4:
                admin.view_items(shah_amanot_hotel)
            elif option == 5:
                product_name = input("Enter product name - ")
                admin.delete_item(shah_amanot_hotel, product_name)
            elif option == 6:
                break
    elif choice == 3:
        print("Exiting...")
        break
