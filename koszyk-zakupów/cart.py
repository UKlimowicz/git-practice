from product import Product
from product import Book

class Cart:

    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)

    def showProducts(self):
        for p in self.products:
            p.showInfo()

    def findProduct(self, name):
        found = False
        for p in self.products:
            if p.name == name:
                found = True
                p.showInfo()
        if not found:
            print("Nie znaleziono productu")       

    def countProducts(self):
        print("Liczba produktów: ", Product.product_count)

    def removeProduct(self, name):
        found = False
        for p in self.products:
            if p.name == name:
                found = True
                self.products.remove(p)
                print("Produk został usunięty")
        if not found:
            print("Produkt nie istnieje")