#python script to determine errors in a robust calculator

class Division:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def safe_divide(numerator, denominator):
        try:
            # Convert inputs to floats
            numerator = float(numerator)
            denominator = float(denominator)
            
            # Perform division inside a try-except block to catch ZeroDivisionError
            result = numerator / denominator
            return f"The result of the division is {result:.2f}"
        
        except ZeroDivisionError:
            # Handle division by zero
            return "Error: Cannot divide by zero."
        
        except ValueError:
            # Handle non-numeric inputs
            return "Error: Please enter numeric values only."
