# Your task is to create a script called dist.py. 
# The program should ask for x and y coordinates for 2 points and calculate the distance between those 2 points. 
# The output should be a float, therefore let's round the result to 2 decimal places.
# The distance should be straight line between the two points.
# The coordinates cannot be negative numbers.

import math


# Define point "p":

x1 = input("Point A, X Coordinate: ")
y1 = input("Point A, Y Coordinate: ")
x2 = input("Point B, X Coordinate: ")
y2 = input("Point B, Y Coordinate: ")

x1 = abs(int(x1))
y1 = abs(int(y1))
x2 = abs(int(x2))
y2 = abs(int(y2))

print(f"The distance between point A and point B is {round((math.sqrt((x2 - x1)**2 + (y2 - y1)**2)), 2)}")
