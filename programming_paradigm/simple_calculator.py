#script of a simple calculator

class SimpleCalculator():
    def add(self, a, b):
        return a+b
    def subtract(self,a,b):
        return a-b  
    def multiply(self, a, b):
        return a*b
    def divide(self, a, b):
        if b == 0:
            raise None
        return a/b
    