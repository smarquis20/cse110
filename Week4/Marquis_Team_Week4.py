"""
Author: Shaun Marquis
Purpose: Team random number guessing game
"""
#imports the random number generator into the game
import random

#sets the initial check so the game will continue
play_again = 'yes'

#checks whether the user would like to play again.  Anything other than yes will exit.
while play_again.lower() == 'yes':

    #initial counter to keep track of the number of guesses.
    counter = 1

    #sets the random magic number
    magic_number = random.randint(1, 100)

    #option to allow user to choose the magic number
    #magic_number = int(input('What is the magic number? '))

    #input from the user to guess the magic number
    guess = int(input('What is your guess? '))

    #logic to process whether or not the user has guess the correct number
    while guess != magic_number:

        #increment counter by one each guess
        counter = counter + 1

        #checks if the magic number needs to be lower
        if magic_number < guess:
            print('Lower')
            guess = int(input('What is your guess? '))
        
        #checks if the magic number needs to be higher
        elif magic_number > guess:
            print('Higher')
            guess = int(input('What is your guess? '))
    
    #if the magic number is guessed it will congradulate the user and ask if they want to play again.
    else:
        print('You guessed it!!')
        print(f'It took you {counter} tries to guess the magic number!')
        play_again = input('Would you like to play again? ')