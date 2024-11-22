class vehicle:
    def __init__(self, brand, seat, price):
        self.brand = brand
        self.seat = seat
        self.price = price

    def info(self):
        print("Brand =", self.brand)
        print("Seat =", self.seat)
        print("Price = ", self.price , '\n')


class car(vehicle):
    def __init__(self, type, brand, seat, price):
        super().__init__(brand, seat, price)
        self.type = type

    def info(self):
        print("Type = ", self.type)
        super().info()
        
class moto(vehicle):
    def __init__(self, type, brand, seat, price):
        super().__init__(brand, seat, price)
        self.type = type

    def info(self):
        print("Type = ", self.type)
        super().info()


vehicle1 = car("Car", "Audi", 4, 25000000)
vehicle1.info()
#print('\n')
vehicle2 = moto("Motorcycle", "Royal Enfield", 2, 3232426)
vehicle2.info()
