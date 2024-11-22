from user import User
from items import Items
from order import Order

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def show_menu(self, restaurant):
        restaurant.menu.view_item()

    def add_item_to_cart(self, restaurant, product_name, quantity):
        product = restaurant.menu.find_item(product_name)
        if product:
            if quantity > product.quantity:
                print("Product quantity exceeded.")
            else:
                temp = Items(product_name=product_name, price=product.price, quantity=quantity)
                product.quantity -= quantity
                self.cart.add_item(temp)
                print("Added to cart!")
        else:
            print("Product not found.")

    def remove_from_cart(self, restaurant, product_name):
        self.cart.remove_from_cart(restaurant, product_name)

    def view_cart(self):
        print("Cart---------------------")
        print(f"{'Product':<20}{'Price':<10}{'Quantity':<10}")
        print("-" * 40)
        for item, quantity in self.cart.items.items():
            print(f"{item.product_name:<20} {item.price:<10}{item.quantity:<10}")
        print("Total price = ", self.cart.total_price)

    def paybill(self):
        price = self.cart.total_price
        if price == 0:
            print("Cart is empty")
        else:
            print(f"Bill {price} paid sucessfully!")
            self.cart.remove_cart()