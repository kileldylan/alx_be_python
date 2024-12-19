#a programm to show multiplication table of a number the user inputs

def multiplication_table():
    print("This is a program to display multiplication tab;le based on input. ")
    number = int(input("Enter a number to see its multiplication table: "))
    
    for i in range(1,11):
        product= number * i
        print(f"{number} * {i} = {product}")
        
multiplication_table()