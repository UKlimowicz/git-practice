
from product import Product
from product import Book
from cart import Cart

# Laptop, 1500, Myszka, 50. Utwórz książkę: Python od podstaw, 120, Jan Kowalski

product1 = Product("Laptop", 1500)
product2 = Product("Myszka", 50)
product3 = Book("Python od podstaw", 120, "Jan Kowalski")

cart = Cart()
cart.addProduct(product1)
cart.addProduct(product2)
cart.addProduct(product3)

cart.showProducts()
cart.countProducts()
cart.findProduct("Laptop")
cart.findProduct("Monitor")
cart.removeProduct("Myszka")
cart.showProducts()