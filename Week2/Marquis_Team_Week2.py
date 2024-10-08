"""
Author: Shaun Marquis

Purpose: Team project to find the area of a square
rectangle and radious of a circle
"""
#Import math module to be able to us PI function
import math

#Get the length of one side of the square
square_l = float(input('\nWhat is the length of a side of the square? '))
#Calculation to get the area of a square
square_area = square_l * square_l
print(f'The area of the square is: {square_area}')

#Get the length and width of the rectangle
rectangle_l = float(input('What is the length of rectangle? '))
rectangle_w = float(input('What is the width of rectangle? '))
#Calculation of the area of the rectangle
rectangle_area = rectangle_l * rectangle_w
print(f'The area of the rectangle is: {rectangle_area}')

circle_r = float(input('What is the radius of the circle? '))
#Calculate area of a circle using the radius given and using the pi function from the math module
circle_area = math.pi * circle_r ** 2
print(f'The area of the circle is: {circle_area}\n')