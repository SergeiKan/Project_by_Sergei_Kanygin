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

# Function to delete a book from the library
def delete_book():
    # Display the list with books
    view_books()
    try:
        book_number = int(input("Enter the book number to delete: "))
        if 1 <= book_number <= len(library):
            removed_book = library.pop(book_number - 1)
            print(f"The book '{removed_book['title']}' has been deleted.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")