import unittest
import calc

#The unittest module provides a rich set of tools for constructing and running tests
#you also need to import the module you want to test

#inherrit class from unittest.Testcase
#A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs
class testCalc(unittest.TestCase):

    #method name must start with test otherwise it will be ignored, its the naming convention
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-10, 5), -5)
        self.assertEqual(calc.add(-10, -5), -15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-10,5), -15)
        self.assertEqual(calc.subtract(-10,-5), -5)

    def test_mul(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-10,-5), 50)
        self.assertEqual(calc.multiply(-10,5), -50)

    def test_div(self):
        self.assertEqual(calc.division(10,5), 2)
        self.assertEqual(calc.division(-10,-5), 2)
        self.assertEqual(calc.division(-10,5), -2)


if __name__=='__main__':
    unittest.main()

