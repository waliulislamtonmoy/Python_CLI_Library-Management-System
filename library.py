import csv
from book import Book

class Library:
    def __init__(self, data_file):
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self):
        books = []
        try:
            with open(self.data_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    authors = row['authors'].split(',')
                    books.append(Book(row['title'], authors, row['isbn'], row['year'], row['price'], row['quantity']))
        except FileNotFoundError:
            pass
        return books

    def save_books(self):
        with open("contact.csv","wt") as csvfile:
            fieldnames = ['title', 'authors', 'isbn', 'year', 'price', 'quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow({
                    'title': book.title,
                    'authors': ','.join(book.authors),
                    'isbn': book.isbn,
                    'year': book.year,
                    'price': book.price,
                    'quantity': book.quantity
                })

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def view_books(self):
        for book in self.books:
            print(book)

    def search_books(self, term):
        result = [book for book in self.books if term.lower() in book.title.lower() or term.lower() in book.isbn.lower()]
        return result

    def search_books_by_author(self, author_name):
        result = [book for book in self.books if author_name.lower() in [author.lower() for author in book.authors]]
        return result

    def remove_book(self, term):
        book_to_remove = None
        for book in self.books:
            if term.lower() in book.title.lower() or term.lower() in book.isbn.lower():
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            return True
        return False

    def lend_book(self, term, borrower):
        for book in self.books:
            if term.lower() in book.title.lower() or term.lower() in book.isbn.lower():
                if book.quantity > 0:
                    book.quantity -= 1
                    book.lent_to.append(borrower)
                    self.save_books()
                    return True
                else:
                    print("Not enough books available to lend.")
                    return False
        print("Book not found.")
        return False

    def view_lent_books(self):
        for book in self.books:
            if book.lent_to:
                print(f"{book.title} lent to {', '.join(book.lent_to)}")

    def return_book(self, term, borrower):
        for book in self.books:
            if term.lower() in book.title.lower() or term.lower() in book.isbn.lower():
                if borrower in book.lent_to:
                    book.quantity += 1
                    book.lent_to.remove(borrower)
                    self.save_books()
                    return True
        print("Book not found or borrower did not lend this book.")
        return False