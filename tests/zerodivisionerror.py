#script to test for ZeroDivisionError

class ZeroDivisionError:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def divide(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.num1 / self.num2
    
def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        division = ZeroDivisionError(num1,num2)
        print(f"{num1} divided by {num2} is {division.divide()}")
    
    except ZeroDivisionError as e:
        print(e)
if __name__ == "__main__":
    main()
        