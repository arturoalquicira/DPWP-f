"""
Arturo Alquicira
DPWP

Mad Lib

"""


"""
Global Variables
"""
name = raw_input("Your name: ")
hometown = raw_input("Your hometown: ")
noun = raw_input("Noun: ")
your_age = raw_input("Your age: ")
random_number = raw_input("Random number: ")
lucky_number = raw_input("Your lucky number: ")

"""
Float
"""

def year_of_birth(age, this_year):
    y = this_year - age
    return y

actual_year = 2014

year = year_of_birth(int(your_age), actual_year)

print year



