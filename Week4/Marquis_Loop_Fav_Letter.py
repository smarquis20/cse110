"""
Author: Shaun Marquis
Purpose: Capitalizes letters in a string.
"""

fav_let = input('What is your favorite letter: ')

word = 'Commitment'
number_of_letters = len(word) # Notice this can now work for any string

for index in range(number_of_letters):
    letter = word[index]
    if letter == fav_let.lower():
        print(f'_', end='')
    else:
        print(f'{letter.lower()}', end='')
print('')