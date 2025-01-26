# script to test the class and static decorators

class Person:
    age = 5
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def display_count(cls, name):
        return cls(name, 0)
    
person_obj = Person("John", 10)
person_obj.display_count("John")
print(person_obj.name)
print(person_obj.age)