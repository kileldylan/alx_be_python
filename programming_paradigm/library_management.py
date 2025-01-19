class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if self._is_checked_out:
            return False  # Cannot check out a book that's already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        if not self._is_checked_out:
            return False  # Cannot return a book that wasn't checked out
        self._is_checked_out = False
        return True

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"Error: '{title}' is already checked out.")
                return
        print(f"Error: '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"Error: '{title}' was not checked out.")
                return
        print(f"Error: '{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available in the library.")
