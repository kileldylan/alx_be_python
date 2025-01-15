#program to generate random numbers between 1 to 10
import random

def unique_number():
    random_number = [random.randint(1,10) for i in range(10)]
    print("Random numbers between 1 to 10 are: ", random_number)
    
    unique_number = set(random_number)
    print("Unique numbers between 1 to 10 are: ", unique_number)
    
unique_number()