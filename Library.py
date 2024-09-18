
'''
Lirary
'''
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability = True
    
    def display(self):
        status = 'Available' if self.availability else 'Rented'
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Status: {status}")


class Patron:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []
    
    def borrow(self, book):
        if book.availability:
            self.borrowed_books.append(book)
            book.availability = False
            print(f"'{book.title}' borrowed by {self.name}.")
        else:
            print(f"'{book.title}' is not available.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.availability = True
            print(f"'{book.title}' returned by {self.name}.")
        else:
            print(f"'{book.title}' not borrowed by {self.name}.")
    
    def list_borrowed_books(self):
        if self.borrowed_books:
            print("Borrowed books:", ", ".join(book.title for book in self.borrowed_books))
        else:
            print("No books borrowed.")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
    
    def add_book(self, book):
        if book.title not in [b.title for b in self.books]:
            self.books.append(book)
            print(f"'{book.title}' added.")
        else:
            print(f"'{book.title}' is already in the library.")
    
    def add_patron(self, patron):
        if patron.name not in [p.name for p in self.patrons]:
            self.patrons.append(patron)
            print(f"Patron '{patron.name}' registered.")
        else:
            print(f"Patron '{patron.name}' is already registered.")
    
    def find_patron(self, name):
        return next((p for p in self.patrons if p.name == name), None)
    
    def find_book(self, title):
        return next((b for b in self.books if b.title == title), None)


def main():
    library = Library()
    
    while True:
        print("\nLibrary Menu")
        print("1. Add book")
        print("2. Register patron")
        print("3. Borrow book")
        print("4. Return book")
        print("5. List borrowed books")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_year = input("Enter publication year: ")
            book = Book(title, author, publication_year)
            library.add_book(book)
        
        elif choice == '2':
            name = input("Enter patron name: ")
            id = input("Enter patron ID: ")
            patron = Patron(name, id)
            library.add_patron(patron)
        
        elif choice == '3':
            name = input("Enter patron name: ")
            title = input("Enter book title: ")
            patron = library.find_patron(name)
            book = library.find_book(title)
            if patron and book:
                patron.borrow(book)
            else:
                print("Patron or book not found.")
        
        elif choice == '4':
            name = input("Enter patron name: ")
            title = input("Enter book title: ")
            patron = library.find_patron(name)
            book = library.find_book(title)
            if patron and book:
                patron.return_book(book)
            else:
                print("Patron or book not found.")
        
        elif choice == '5':
            name = input("Enter patron name: ")
            patron = library.find_patron(name)
            if patron:
                patron.list_borrowed_books()
            else:
                print("Patron not found.")
        
        elif choice == '6':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()