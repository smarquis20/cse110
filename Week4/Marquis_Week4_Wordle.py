"""
Author: Shaun Marquis
Purpose: Week 4 wordle guessing game
"""
#For extra credit i created a list of words and used the random choice function to choose a random word from the list. 

import random

#list of possible secret words
secret_list = ['stake', 'overflow', 'ward', 'temple', 'priesthood', 'church', 'bishopric']

#set the secret word
secret_word = random.choice(secret_list)

#initiate tracker for number of guesses
number_guess = 1

#set variable for secret word length
secret_number_of_letters = len(secret_word)

print('Welcome to the word guessing game!')
print(f'The secret word has {secret_number_of_letters} letters.\n')

#sets the initial hint with correct length according to the length of the secret word
print('Hint: ',end='')
for i in range(secret_number_of_letters):
    print(f'_', end='')


#get guess from user
guess = input('\nWhat is your guess? ')
guess = guess.lower()
#set variable for user guess length
guess_number_of_letters = len(guess)

#while loop will continue to ask for guess until the user guesses the correct word
while guess != secret_word:

    #increment number of guesses with each failed guess
    number_guess = number_guess + 1

    #if statement to do error checking to make sure the user is only putting the same number of characters as the secret word
    if guess_number_of_letters == secret_number_of_letters:

        print('Hint: ',end='')

        #for loop to pull each letter out of the secret word and put into an array
        for i in range(secret_number_of_letters):
            letter_secret = secret_word[i]

        #for loop to pull each letter out of the user guess word and put into an array
        for i in range(guess_number_of_letters):
            letter_guess = guess[i]

            #compares each letter in guess and secret words and if in the same location it will capitalize the letter
            if guess[i] == secret_word[i]:
                print(f'{guess[i].capitalize()}', end='')
            #compares each letter in the guess word with the entire secret word. If found it will print the lowercase letter
            elif guess[i] in secret_word:
                print(f'{guess[i]}', end='')
            #will print and underscore if the letter is not in the secret word at all
            else:
                print(f'_', end='')
        
        #Will continue to ask the user for a guess until they guess the correct word
        guess = input('\nWhat is your guess? ')
        guess = guess.lower()
        guess_number_of_letters = len(guess)
    else:
        #Error message to the user if they put in too many or too few characters
        print(f'You can only use {secret_number_of_letters} characters in your guess.')
        guess = input('\nWhat is your guess? ')
        guess = guess.lower()
        guess_number_of_letters = len(guess)
print('')
#will print you win if the word is guessed correctly and will print out the number of tries
print(f'You win!!! It took you {number_guess} guesses!')