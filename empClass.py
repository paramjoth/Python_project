class Employee():

    raise_amount = 1.05

    def __init__(self, fname, lname, pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay

    def email(self):
        return '{}.{}@company.com'.format(self.fname, self.lname)

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def payraise(self):
        self.pay = int(self.pay * self.raise_amount)