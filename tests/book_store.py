#script to calculate final price after taxing

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"Title: {self.title}, Author:{self.author}, Price:{self.price}"
    
class Ebook(Book):
    def __init__(self, filesize):
        self.filesize = filesize
    def __str__(self):
        return f"Title: {self.title}, Author:{self.author}
                Price:{self.price}, File Size(mb): {self.filesize}"
   
class Tax:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate
    
    def calculate_tax(self, book):
        return book.price * (1 + self.taxrate )
class FinalPrice(Book,Ebook,Tax):
    def __inti__(self, book, tax):
        self.book = book
        self.tax = tax
    
    def calculate_final_price(self):
        return self.book.price + self.tax.calculate_tax(self.book)

        
    
    
    
        