#script to calculate total price of stock in catalogue

class Products:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_price(self):
        return self.price * self.quantity
    
def main():
    print("Welcome to the Products Total Price calculator!")
    
    try:
        name = input("Enter the product name: ")
        price = input("Enter the product price: ")
        quantity = input("Enter the product quantity: ")
        if not price.replace('.', '', 1).isdigit() or not quantity.isdigit():
            raise ValueError("Invalid price or quantity. Please enter a numeric value.")
        
        price = float(price)
        quantity = int(quantity)
        product = Products(name, price, quantity)
        print(f"The total price of {quantity} {name} is Ksh {product.total_price():.2f}")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
        