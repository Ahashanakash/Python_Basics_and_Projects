class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.product_name.lower() == item_name.lower():
                return item

    def delete_item(self, product_name):
        item = self.find_item(product_name)
        if item:
            self.items.remove(item)
            print(f"Item {product_name} deleted")
        else:
            print("Item not found")

    def view_item(self):
        print("Menu ---------------------")
        print(f"{'Name':<20}{'Price':<10}{'Quantity':<10}")
        print("-" * 40)
        for item in self.items:
            print(f"{item.product_name:<20}{item.price:<10}{item.quantity:<10}")