#program to handle multiple calculations with diff operations.

def match_case_calculator():
    print("Welcome to our calculator")
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")
    
    match operation:
        case _ if operation == "+":
            calculation = num1 + num2
            print("The result is :", calculation)
        case _ if operation == "-":
            calculation = num1 - num2
            print("The result is :", calculation)
        case _ if operation == "*":
            calculation = num1 * num2
            print("The result is :", calculation)
        case _ if operation == "/":
            calculation = num1 / num2
            print("The result is :", calculation)
match_case_calculator()