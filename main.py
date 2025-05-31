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


# Create list for book`s information in library
library = []

# Add a new book in library
def add_book():
    title = input("Enter book title: ")
    author = input("Enter an author: ")
# Add the book to the list
    library.append({"title": title, "author": author, "user": None})
    print("The book was successfully added!")

# Function to display all books in the library
def view_books():
    if not library:
        print("The library is empty.")
    else:
        print("List of books: ")
        for index, book in enumerate(library, start=1):
            print(f"{index}. {book['title']} - {book['author']}")

# Function to delete book from the library
def delete_book():
    # Display the list with books
    view_books()
    try:
        book_number = int(input("Enter the book number for delete: "))
        if 1 <= book_number <= len(library):
            removed_book = library.pop(book_number - 1)
            print(f"The book '{removed_book['title']}' was deleted.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter valid number.")

# Function for searching books by title or author
def search_book():
    keyword = input("Enter name of book or author to search: ").lower()
    # Create the dictionary with indexes and books for easier searching
    library_dict = {index: book for index, book in enumerate(library, start=1)}
    # Filter books that contain the keyword in the title or author name
    results = {index: book for index, book in library_dict.items() 
               if keyword in book['title'].lower() or keyword in book['author'].lower()}
    if results:
        print("Books found: ")
    else:
        print("No books found.")

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
