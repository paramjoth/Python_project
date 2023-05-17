#object-oriented programming
import datetime


class property_details():
    #class variable
    num_of_property_types = 0
# instance variables - unique for each instance - style, price, year_built, stories are instance variables
    def __init__(self, style, price, year_built, stories):
        self.style = style
        self.price = price
        self.year_built = year_built
        self.stories = stories
        self.substyle = style + ' - ' + stories

        property_details.num_of_property_types += 1

    def new_construction(self):
        if self.year_built > 2021:
            return 'Y'
        else:
            return 'N'

    @classmethod
    def from_string(cls, emp_str):
        style, stories = emp_str.split('-')
        return cls(style, stories)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


my_date = datetime.date(2022, 8, 21)

print(property_details.is_workday(my_date))

style_1 = property_details('Residential', 700000, 2022, '2 stories')
style_2 = property_details('Commercial', 1000000, 2020, '1 story')
style_3 = property_details('Commercial', 1000000, 2020, '1 story')
style_3 = property_details('Commercial', 1000000, 2021, '1 story')

print(style_3.__dict__)
print(style_1.new_construction())
print(property_details.num_of_property_types)

#########################################################################
#class variables - should be same for all instance
########################################################################




####################################
#regular methods, class methods, stati methods
####################################
#regular methods in a class automatically takes the instance (self) as first argument


#class methods automatically pass class 'cls' as the first argument
    # @classmethod
    # def from_string(cls, emp_str):
    #     style, stories = emp_str.split('-')
    #     return cls(style, stories)


#static method dont pass anything automatically, they are regular function but we include those in a class because they have some logical connection with the class


#subclass - inheritance
