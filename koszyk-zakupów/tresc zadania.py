# ==================================================
# ZADANIE 9 – KOSZYK ZAKUPÓW
# ==================================================
# CEL: Przećwicz: klasy, obiekty, __init__(), self, isinstance(), import,
# from ... import ...,  listy obiektów, count..., find..., remove...
# dziedziczenie, super()
# ==================================================
# CZĘŚĆ 1 – KLASA PRODUCT
# ==================================================
# Utwórz plik, product.py. Stwórz klasę Product. Konstruktor powinien przyjmować:
# name, price. Sprawdź: name musi być typu str, price musi być typu int lub float
# Jeżeli dane są poprawne self.name = name, self.price = price 
# Dodaj metodę showInfo() która wyświetli: Laptop 1500
# ==================================================
# CZĘŚĆ 2 – KLASA BOOK
# ==================================================
# W tym samym pliku utwórz klasę Book. Book ma dziedziczyć po:Product
# Konstruktor powinien przyjmować: name, price, author.Użyj super()
# aby przekazać: name price do klasy Product.
# Dodaj self.author = author.Nadpisz metodę: showInfo()
# tak aby wyświetlała: Python od podstaw 120 Jan Kowalski
# ==================================================
# CZĘŚĆ 3 – KLASA CART
# ==================================================
# Utwórz plik cart.py. Zaimportuj Product oraz Book
# Stwórz klasę Cart. W konstruktorze utwórz: self.products = []
# Dodaj metodę addProduct(product),która dodaje produkt do koszyka.
# Dodaj metodę showProducts(), która wyświetla wszystkie produkty.
# Dodaj metodę countProducts(), która wyświetla: Liczba produktów: X
# Dodaj metodę findProduct(name). Jeżeli produkt istnieje, wyświetl: jego dane.
# Jeżeli produkt nie istnieje, wyświetl: Nie znaleziono produktu.
# ==================================================
# NOWA CZĘŚĆ ⭐
# ==================================================
# Dodaj metodę removeProduct(name).Jeżeli produkt istnieje - usuń go z listy.
# wyświetl: Produkt usunięty. Jeżeli produkt nie istnieje, wyświetl:
# Nie znaleziono produktu.
# ==================================================
# CZĘŚĆ 4 – TESTOWANIE
# ==================================================
# Utwórz plik main.py. Zaimportuj: Product, Book, Cart. Utwórz produkty:
# Laptop, 1500, Myszka, 50. Utwórz książkę: Python od podstaw, 120, Jan Kowalski
# Utwórz: cart = Cart(). Dodaj wszystkie produkty do koszyka.
# Wywołaj: showProducts(), countProducts(), findProduct("Laptop"),
# findProduct("Monitor"), removeProduct("Myszka"), showProducts()
# ==================================================
# OCZEKIWANY WYNIK
# ==================================================
# Laptop 1500
# Myszka 50
# Python od podstaw 120 Jan Kowalski
# Liczba produktów: 3
# Laptop 1500
# Nie znaleziono produktu.
# Produkt usunięty.
# Laptop 1500
# Python od podstaw 120 Jan Kowalski
# ==================================================
# PODPOWIEDŹ
# ==================================================
# Nowością w tym zadaniu jest: class Book(Product) oraz: super().__init__(...)
# Reszta projektu opiera się na tym samym schemacie, który ćwiczyłaś już w:
# - Classroom,- Library,- MovieCollection, - GameCollection,- Academy
#