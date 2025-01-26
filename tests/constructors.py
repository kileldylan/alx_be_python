#script to test constructors and destructors in python

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Tax:
    def __init__(self, tax):
        self.tax = tax
    
    def __str__(self):
        return f"{self.tax}"
    
    def tax_calculate(self, product):
        return product.price * (1 + self.tax)

class FinalPrice(Product, Tax):
    def __init__(self, name, price, tax):
        super().__init__(name, price)
        Tax.__init__(self, tax)
    
    def calc_final_price(self):
        return self.tax_calculate(self)
    
tax_rate = FinalPrice("Shoe", 200, 0.05)
print(f"Product: {tax_rate.name}, Price: {tax_rate.price}, Tax: {tax_rate}")
        