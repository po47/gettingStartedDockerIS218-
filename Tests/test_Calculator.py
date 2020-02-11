import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(2, 3)
        self.assertEqual(float(-1), float(result))

    def test_calculator_return_product(self):
        result = self.calculator.Product(2, 2)
        self.assertEqual(4, result)

    def test_calculator_return_quotient(self):
        result = self.calculator.Quotient(2, 4)
        self.assertEqual(0.5, result)

    def test_calculator_return_root(self):
        result = self.calculator.Root(169, 2)
        self.assertEqual(13, result)

    def test_calculator_return_power(self):
        result = self.calculator.Power(13, 2)
        self.assertEqual(169, result)

    def test_calculator_return_log(self):
        result = self.calculator.Logarithm(10, 1)
        self.assertEqual(0, result)

    #other defs
    def test_calculator_access_difference_result(self):
        self.calculator.Difference(3, 2)
        self.assertEqual(float(1), self.calculator.Result)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(5, 4)
        self.assertEqual(9, self.calculator.Result)

    def test_calculator_access_product_result(self):
        self.calculator.Product(3, 2)
        self.assertEqual(6, self.calculator.Result)

    def test_calculator_access_quotient_result(self):
        self.calculator.Quotient(8, 4)
        self.assertEqual(2, self.calculator.Result)


    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()

        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)


if __name__ == '__main__':
    unittest.main()
