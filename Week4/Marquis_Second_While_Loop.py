"""
Author: Shaun Marquis

Purpose: Practice while loops.
"""

answer = input('May I have a piece of candy? ')

while answer.lower() != 'yes':
    answer = input('May I have a piece of candy? ')

print('Thank you.')