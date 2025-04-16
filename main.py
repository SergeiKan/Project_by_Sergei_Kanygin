# Create list for book`s information in library
library = []

# Add a new book in library
def add_book():
    title = input("Enter book title: ")
    author = input("Enter an author: ")
# Add the book to the list
    library.append({"title": title, "author": author})
    print("The book was successfully added!")

add_book()
print(f"Library: {library}")