
"""
Name
Date
Assignment Name
"""

'''
name= raw_input("Enter Your Name: ")

print name + "Very nice to meet you!"

'''


# single line comment

# Expressions

first = "Arturo"
yearBorn = 1991
currentYear = 2014
age = currentYear - yearBorn
age += 1
print(age)

# Conditionals

budget = 300

if budget > 200:
    # stuff would wanna do if true
    budget += 1
    print "you can buy vans"
elif budget > 30:
    print "you can buy Jordans"
else:
    print "no shoes for you"

# pass (if you have an empty conditional and need it to ignore)

# functions

def calcArea(h, w):
    perimeter = 2*h + 2*w
    a = h*w
    return a

height = 40
width = 30

area = calcArea(height, width)
# Casting
# print "You area:" + (area) #int #float

# Arrays
students = ["Jairo", "Arturo", "Austin"]

# Dictionaries - associative arrays
villains = dict()
villains = {"Star Wars":"Darth Vader", "Lion King":"Scar"}

print villains["Star Wars"]
print students[1:3]

# Loops
x = 100
for i in range(100, 0, -1):
    x -= 1
    print "There are: " + str(x) + " number of balls"
    pass

for s in students:
    print s + " you are the coolest!"

# format method for big strings
your_name = "Arturo"
real_age = 23

message = '''
{your_name}, thanks for joining us!
    You are {real_age}
'''

message = message.format(**locals())
print message


import random
import decimal
for y in range(0, 100):
    print decimal.Decimal(random.randrange(4000))/10000
