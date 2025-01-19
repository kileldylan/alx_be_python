#script to test the simple calculator
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
        
    def test_add(self):
        self.assertEqual(self.calc.add(20,5),25)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(20,5),15)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(20,5),100)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(20,5),4)

if __name__ == "__main__":
    unittest.main()