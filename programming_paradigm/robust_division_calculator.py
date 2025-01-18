#python script to determine errors in a robust calculator

class Division:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def safe_divide(self,numerator, denominator):
        try:
            numerator = float(numerator)
            denominator = float(denominator)
            
            if denominator == 0:
                raise ZeroDivisionError("Number cannot be divided by zero!")
            else:
                results = numerator/denominator
                return print(f"The result of {numerator} divided by {denominator} is {results}")
        except ValueError as e:
            print(e)
    