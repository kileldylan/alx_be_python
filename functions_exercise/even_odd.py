# A function that takes an integer as input, and prints "Even" if the integer is even, or "Odd" if the integer is odd.
def even_odd(n):
    
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
even_odd(n = int(input("Enter a number: ")))