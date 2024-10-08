"""
Author: Shaun Marquis

Purpose: Compare Numbers using if else statements
"""

#Get the numbers from users to compare
grade = int(input('\nWhat is your grade percentage: '))

#If statement to decide if number 1 is larger than number 2
#if grade >= 90:
#    print('Your class grade: A')
#elif grade >= 80:
#    print('Your class grade: B')
#elif grade >= 70:
#    print ('Your class grade: C')
#elif grade >= 60:
#    print('Your class grade: D')
#elif grade < 60:
#    print('Your class grade: F')

#if grade >= 70:
#    print('Congratulations you passed the class!')
#else:
#    print('You failed the class. Better luck next time.')



#If statement to decide if number 1 is larger than number 2
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
elif grade < 60:
    letter = 'F'

print(f'Your class grade: {letter}')

if grade >= 70:
    print('Congratulations you passed the class!')
else:
    print('You failed the class. Better luck next time.')