from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.exponent import Exponent
from MathOperations.root import Root
from MathOperations.log import Log
from MathOperations.division import Division 

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Product(self, a,b):
        self.Result= Multiplication.product(a,b)
        return self.Result

    def Quotient(self, a,b):
        self.Result= Division.quotient (a,b)
        return self.Result

    def Root(self, a, b):
        self.Result = Root.root(a, b)
        return self.Result

    def Power(self, a, b):
        self.Result = Exponent.power(a, b)
        return self.Result

    def Logarithm(self, a, b):
        self.Result = Log.logarithm(a, b)
        return self.Result




