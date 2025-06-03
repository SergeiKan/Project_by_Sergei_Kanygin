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

    def bubble_sort_books(self):  # Сортировка пузырьком / Bubble sort
        start = time.time()
        n = len(self.books)
        for i in range(n):
            for j in range(0, n - i - 1):
                a = self.books[j]
                b = self.books[j + 1]
                if (a.year > b.year) or (a.year == b.year and not a.evaluate_expression() and b.evaluate_expression()):
                    self.books[j], self.books[j + 1] = b, a
        end = time.time()
        print(f"Время сортировки пузырьком: {end - start:.6f} сек / Bubble sort time: {end - start:.6f} seconds")

    def merge_sort_books(self):   # Merge sort
        start = time.time()
        self.books = self._merge_sort(self.books)
        end = time.time()
        print(f"Merge sort time: {end - start:.6f} seconds")

    def _merge_sort(self, books):   # Recursive part
        if len(books) <= 1:
            return books
        mid = len(books) // 2
        left = self._merge_sort(books[:mid])
        right = self._merge_sort(books[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):  # Merge
        result = []
        while left and right:
            a = left[0]
            b = right[0]
            if (a.author < b.author) or (a.author == b.author and a.evaluate_expression() and not b.evaluate_expression()):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result
        
    def load_from_csv(self, filename):
        try:
            df = pd.read_csv(filename)
            for _, row in df.iterrows():
                book = Book(
                    title=row['title'],
                    author=row['author'],
                    year=int(row['year']),
                    logic_expression=row['expression'],
                    is_scientific=bool(row['scientific']),
                    is_fiction=bool(row['fiction'])
                )
                self.add_book(book)
            print(f"File '{filename}' loaded successfully.")
        except Exception as e:
            print(f"Error loading CSV file: {e}")

    def save_to_csv(self, filename):
        try:
            data = [{
                'title': b.title,
                'author': b.author,
                'year': b.year,
                'expression': b.logic_expression,
                'scientific': b.is_scientific,
                'fiction': b.is_fiction
            } for b in self.books]
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            print(f"Data saved to '{filename}'.")
        except Exception as e:
            print(f"Error saving CSV file: {e}")

def main_menu():
    library = Library()

    while True:
        print("\n Menu ---")
        print("1. Add book")
        print("2. View books")
        print("3. Delete book")
        print("4. Search by title/author")
        print("5. Search by logic result")
        print("6. Bubble sort")
        print("7. Merge sort")
        print("8. Load from CSV")
        print("9. Save to CSV")
        print("0. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            expr = input("Logic (example, scientific and not fiction): ")
            is_scientific = input("Is this fiction? (True/False): ").lower() == "true"
            is_fiction = input("Is this scientific? (True/False): ").lower() == "true"
            book = Book(title, author, year, expr, is_scientific, is_fiction)
            library.add_book(book)
            elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.view_books()
            index = int(input("Введите номер книги для удаления / Enter book number to delete: ")) - 1
            library.delete_book(index)
        elif choice == "4":
            keyword = input("Введите ключевое слово / Enter keyword: ")
            results = library.search_books(keyword)
            for book in results:
                print(f"- {book.title}, логика: {book.logic_expression}, результат: {book.evaluate_expression()}")









# Run the code
if __name__ == "__main__":
    main()
