"""
Author: Shaun Marquis

Purpose: Clever Story - Ask user for random words and insert those
answers into the story.
"""
#Adding additional sentences and random words from the user for extra credit.  Adding two more verbs
#and one more adjective to the inputs.

#Gather required input from the user
print('\nPlease enter the following: ')
adjective_1 = input('\nadjective: ')
animal = input('animal: ')
verb_1 = input('verb: ')
exclamation = input('exclamation: ')
verb_2 = input('verb: ')
verb_3 = input('verb: ')
#extra credit inputs
adjective_2 = input('adjective: ')
verb_4 = input('verb: ')
verb_5 = input('verb: ')

#Story with variables added
print('\nThe other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective_1.lower()} {animal.lower()} {verb_1.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {verb_2.lower()} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb_3.lower()}')
print('right in front of my family.\n')
#extra credit story addition
print(f'Later that night a group of farm animals formed a {adjective_2.lower()} bond with my family.')
print(f'They {verb_4.lower()} our family and taught us their ways.  We now know how to {verb_5.lower()}')
print('and we will live their ways.\n')