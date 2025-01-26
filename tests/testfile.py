#script to display student information

class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
            print(f"Name: {self.name}, Age: {self.age}")

def main():
    print("Welcome to the Student Information Tool!")
    
    try:
        name = input("Enter the student's name: ")
        age = input("Enter the student's age: ")
        if not age.isdigit():
            raise ValueError("Invalid age. Please enter a numeric value.")
        
        age = int(age)
        student = Students(name, age)
        student.display()
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()