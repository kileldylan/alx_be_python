# Custom exception class
class ValueTooHighError(Exception):
    """Exception raised when the value is too high."""
    def __init__(self, value, message="Value exceeds the limit of 100."):
        self.value = value
        self.message = message
        super().__init__(f"{self.message} (Value provided: {self.value})")

# Class to handle the logic
class NumberChecker:
    def __init__(self):
        # Constructor for any initialization, if needed
        pass

    def check_value(self, number):
        """Check if the number is greater than 100 and raise ValueTooHighError."""
        if number > 100:
            raise ValueTooHighError(number)
        else:
            print(f"The number {number} is within the allowed range.")

# Main program
if __name__ == "__main__":
    checker = NumberChecker()
    
    try:
        num = int(input("Enter a number: "))
        checker.check_value(num)
    except ValueTooHighError as e:
        print(f"Custom Exception Caught: {e}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
