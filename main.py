import pandas as pd
import time
from abc import ABC, abstractmethod

class AbstractBook(ABC):   # Abstract class for book basical format
    @abstractmethod
    def evaluate_expression(self):
        pass
    @abstractmethod
    def is_available(self):
        pass

class Book(AbstractBook):   # Base book class
    def __init__(self, title, author, year, logic_expression, is_scientific, is_fiction):
        self.title = title
        self.author = author
        self.year = year
        self.logic_expression = logic_expression
        self.is_scientific = is_scientific
        self.is_fiction = is_fiction
        self.user = None

    def is_available(self):   # Check if book is available
        return self.user is None

    def evaluate_expression(self):
        try:
            expr = self.logic_expression.replace("and", "and").replace("or", "or").replace("not", "not")
            return eval(expr, {}, {
                "scientific": self.is_scientific,
                "fiction": self.is_fiction
            })
        except Exception:
            return False

class PrintedBook(Book):   # Subclass for printed books
    def __init__(self, title, author, year, logic_expression, is_scientific, is_fiction, pages):
        super().__init__(title, author, year, logic_expression, is_scientific, is_fiction)
        self.pages = pages

class DigitalBook(Book):   # Subclass for digital books
    def __init__(self, title, author, year, logic_expression, is_scientific, is_fiction, file_size_mb):
        super().__init__(title, author, year, logic_expression, is_scientific, is_fiction)
        self.file_size_mb = file_size_mb

    def evaluate_expression(self):
        return self.is_scientific

class Library:   # Create list for book`s information in library
    def __init__(self):
        self.books = []
        self.books_by_year = {}   # Books grouped by year
        self.additional_info = {}
        self.book_year_range = ()   # Year range tuple

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Book list:")
            for idx, book in enumerate(self.books, start=1):
                status = "Available" if book.is_available() else f"Borrowed by {book.user}"
                print(f"{idx}. {book.title} ({book.author}, {book.year}) - {status}")

    def delete_book(self, index):
        if 0 <= index < len(self.books):
            removed = self.books.pop(index)
            print(f"Book '{removed.title}' deleted.")
        else:
            print("Invalid book number.")

    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]

    def search_books_by_logic(self, expected_value=True):  # Logic-based search
        return [book for book in self.books if book.evaluate_expression() == expected_value]








# Function to mark book as borrowed
def borrow_book():
    view_books()
    try:
        book_number = int(input("Enter the book number: "))
        if 1 <= book_number <= len(library):
            book = library[book_number - 1]
            if book['user']:
                print(f"The book is already borrowed by {book['user']}.")
            else:
                user = input("Enter your name: ")
                book['user'] = user
                print(f"The book '{book['title']}' has been successfully borrowed by {user}.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter valid number.")

# Function for book returning
def return_book():
    view_books()
    try:
        book_number = int(input("Enter the book number wich you want to return: "))
        if 1 <= book_number <= len(library):
            book = library[book_number - 1]
            if not book['user']:
                print("This book in the library.")
            else:
                book['user'] = None
                print(f"The book '{book['title']}' was successfully returned.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter valid number.")

# Main menu
def main():
    while True:
        print("\nMenu:")
        print("1. Add the book in list")
        print("2. View list of books")
        print("3. Delete the book")
        print("4. Search the book in library")
        print("5. Borrow the book")
        print("6. Return the book")
        print("7. Exit")
        choice = input("Choose an action (1-7): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            borrow_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the code
if __name__ == "__main__":
    main()
