#script to test the simple calculator
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(20,5),25)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(20,5),15)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(20,5),100)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(20,5),4)

if __name__ == "__main__":
    unittest.main()