"""
Author: Shaun Marquis

Purpose: Compare Numbers using if else statements
"""

#Get the numbers from users to compare
number_1 = int(input('\nEnter a value for int 1: '))
number_2 = int(input('Enter a value for int 2: '))

#If statement to decide if number 1 is larger than number 2
if number_1 > number_2:
    print('The first number is greater.')
else:
    print('The first number is not greater.')

if number_1 == number_2:
    print ('The numbers are equal.')
else:
    print('The numbers are not equal.')

if number_2 > number_1:
    print('The second number is greater.')
else:
    print('The second number is not greater.')

fav_animal = input('\nWhat is your favorite animal? ')
fav_animal = fav_animal.lower()

if fav_animal == 'bear':
    print('That''s my favorite animal too!')
else:
    print('That one is not my favorite.')