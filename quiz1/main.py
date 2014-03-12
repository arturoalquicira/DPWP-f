"""
Arturo Alquicira
"""



# First Function

# width = raw_input("Width: ")
# height = raw_input("Height: ")
#
# def calcArea(w, h):
#     a = w*h
#     return a
#
# area = calcArea(int(width), int(height))
#
# if width == height:
#     print "The area of your square is " + str(area) + " square feet."
# else:
#     print "The area of your rectangle is " + str(area) + " square feet."


# Loop

number_of_bottles = 99

for i in range(number_of_bottles, 0, -1):
    number_of_bottles -= 1
    print str(i) + " Bottles of beer on the wall, " + str(i) + " Bottles of beer... take one down and pass it around. Now you have " + str(number_of_bottles) + " bottles of beer on the wall!"

