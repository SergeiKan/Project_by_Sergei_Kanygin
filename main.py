# Create list for book`s information in library
library = []

# Add a new book in library
def add_book():
    title = input("Enter book title: ")
    author = input("Enter an author: ")

# Add the book to the list
    library.append({"title": title, "author": author})
    print("The book was successfully added!")

# Function to display all books in the library
def view_books():
    if not library:
        print("The library is empty.")
    else:
        print("List of books: ")
        for index, book in enumerate(library, start=1):
            # Check if book is borrowed by user and add information
            user_info = f" (borrowed by: {book['user']})" if book['user'] else " (available)"
            print(f"{index}. {book['title']} - {book['author']}{user_info}")