import unittest
from empClass import Employee

class test_employee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee('Param', 'Chahal', 5000)
        self.emp2 = Employee('Srikanth', 'Pandem', 8000)


    def test_email(self):
        self.assertEqual(self.emp1.email, 'Param.Chahal@company.com')
        self.assertEqual(self.emp2.email, 'Srikanth.Pandem@company.com')

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'Param Chahal')
        self.assertEqual(self.emp2.fullname, 'Srikanth Pandem')

    def test_payraise(self):
        self.emp1.payraise()
        self.emp2.payraise()
        self.assertEqual(self.emp1.pay, 5250)
        self.assertEqual(self.emp2.pay, 8400)


if __name__=='__main__':
    unittest.main()
