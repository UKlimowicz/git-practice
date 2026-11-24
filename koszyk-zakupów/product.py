
class Product:

    product_count = 0

    def __init__(self, name, price):

        if not isinstance (name, str):
            return
        if not isinstance (price, (int, float)):
            return
        self.name = name
        self.price = price
        Product.product_count += 1

    def showInfo(self):
        print(self.name, self.price)

class Book(Product):

    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def showInfo(self):
        print(self.name, self.price, self.author)