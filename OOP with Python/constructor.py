class Pen:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color 
        self.price = price

amar_pen = Pen("Matador","Black", 5)
print(amar_pen.brand, amar_pen.color, amar_pen.price)

tomar_pen = Pen("cello","red", 15)
print(tomar_pen.brand, tomar_pen.color, tomar_pen.price)

tader_pen = Pen("BIC","Yellow", 10)
print(tader_pen.brand, tader_pen.color, tader_pen.price)