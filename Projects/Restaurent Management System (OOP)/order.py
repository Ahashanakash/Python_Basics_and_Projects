class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, product):
        if product in self.items:
            self.items[product] += product.quantity
        else:
            self.items[product] = product.quantity

    def remove_from_cart(self, restaurant, product_name):

        for item in self.items.keys():
            if item.product_name.lower() == product_name.lower():
                product = restaurant.menu.find_item(product_name)
                if product:
                    product.quantity += self.items[item]
                del self.items[item]
                print(f"Product {product_name} removed from cart.")
                return
        print("Product not found in cart.")

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def remove_cart(self):
        self.items = {}