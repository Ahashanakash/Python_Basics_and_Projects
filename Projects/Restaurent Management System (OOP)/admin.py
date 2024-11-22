from user import User

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employees(self, restaurant, employee):
        restaurant.add_employees(employee)

    def view_employees(self, restauternt):
        restauternt.view_employees()

    def add_items(self, restaurant, item):
        restaurant.menu.add_item(item)

    def view_items(self, restaurant):
        restaurant.menu.view_item()

    def delete_item(self, restaurant, product_name):
        restaurant.menu.delete_item(product_name)