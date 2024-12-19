#python script to print square pattern

#define the function
def python_drawing():
    
    #input the desired size of the square
    size = int(input("Enter the size of the pattern: "))
    
    #validate if the input is a positive number
    if size <= 0:
        print("Please enter a positive number")
        return
    row = 0
    
    while row < size:
        for col in range(size):
            print("*", end="")
        print()
        row += 1
        
python_drawing()