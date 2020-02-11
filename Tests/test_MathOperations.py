import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponent import Exponent
from MathOperations.root import Root
from MathOperations.log import Log

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Sum(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_Subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_Sum_list(self):
        numlist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(numlist))

    def test_MathOperations_Product(self):
        self.assertEqual(18, Multiplication.product(6,3))

    def test_MathOperations_Product_list(self):
        numlist= [2,3,4]
        self.assertEqual(24, Multiplication.product(numlist))

    def test_MathOperations_Quotient(self):
        self.assertEqual(2, Division.quotient(6,3))

    def test_MathOperations_root(self):
        self.assertEqual(13, Root.root(169, 2))

    def test_MathOperations_exponent(self):
        self.assertEqual(16, Exponent.power(4, 2))

    def test_MathOperations_logarithm(self):
        self.assertEqual(0, Log.logarithm(10, 1))


if __name__ == '__main__':
    unittest.main()
