from library import Library
from book import Book

def menu():
    print("\n Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Books")
    print("4. Search Books by Author")
    print("5. Remove Book")
    print("6. Lend Book")
    print("7. View Lent Books")
    print("8. Return Book")
    print("9. Exit")

def main():
    library = Library('data/books.csv')

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            authors = input("Enter authors (comma separated): ").split(',')
            isbn = input("Enter ISBN: ")
            year = input("Enter publishing year: ")
            price = input("Enter price: ")
            quantity = input("Enter quantity: ")
            book = Book(title, authors, isbn, year, price, quantity)
            library.add_book(book)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            term = input("Enter title or ISBN to search: ")
            results = library.search_books(term)
            for book in results:
                print(book)

        elif choice == '4':
            author_name = input("Enter author name to search: ")
            results = library.search_books_by_author(author_name)
            for book in results:
                print(book)

        elif choice == '5':
            term = input("Enter title or ISBN to remove: ")
            if library.remove_book(term):
                print("Book removed successfully.")
            else:
                print("Book not found.")

        elif choice == '6':
            term = input("Enter title or ISBN to lend: ")
            borrower = input("Enter borrower's name: ")
            if library.lend_book(term, borrower):
                print("Book lent successfully.")
        
        elif choice == '7':
            library.view_lent_books()

        elif choice == '8':
            term = input("Enter title or ISBN to return: ")
            borrower = input("Enter borrower's name: ")
            if library.return_book(term, borrower):
                print("Book returned successfully.")

        elif choice == '9':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()