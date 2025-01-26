#script to test OOP Fundamentals in python

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def borrow_book():
        if is_borrowed:
            return False
        
        is_borrowed = True
        return True
    
    def return_book():
        if not is_borrowed:
            return False
        is_borrowed = False
        return True

    def is_available(self):
        return not self.is_borrowed
    
class Library:
        
        def __init__(self):
             self._books = []
        
        def add_book(self, book):
            self.books.append(book)
        
        def borrow_books(self, title):
            for book in self._books:
                if book.title == title:
                    if book.borrow_book():
                        print(f"'{title}' Succesfully borrowed the book!.")
                    else:
                        print(f"Error: '{title}' is already borrowed.")
                    return
            print(f"Error: '{title}' not found in the library.")
            
        def return_books(self, title):
            for book in self._books:
                if book.title == title:
                    if book.return_book():
                        print(f"'{title}' has been returned.")
                    else:
                        print(f"Error: '{title}' was not borrowed.")
                    return
                print("Error '{title}' not found in the library!")
                
        def list_available_books(self):
            available_books = [book for book in self._books if book.is_available()]
            if available_books:
                for book in available_books:
                    print(f"{book.title} by {book.author}")
            else:
                print("No books available in the library.")
                