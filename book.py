class Book:
    def __init__(self, title, authors, isbn, year, price, quantity):
        self.title = title
        self.authors = authors  # List of authors
        self.isbn = isbn
        self.year = year
        self.price = float(price)
        self.quantity = int(quantity)
        self.lent_to = []

    def __str__(self):
        return f"Title: {self.title}, Authors: {', '.join(self.authors)}, ISBN: {self.isbn}, Year: {self.year}, Price: ${self.price}, Quantity: {self.quantity}"