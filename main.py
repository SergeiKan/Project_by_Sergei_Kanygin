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