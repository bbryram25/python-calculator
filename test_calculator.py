import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 2), 4)

    # Add the following test methods to the TestCalculator class:
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(10, 2), 8)
   
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 10), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):  # Fixed typo from devide to divide
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(7, 5), 2)


if __name__ == '__main__':
    unittest.main()