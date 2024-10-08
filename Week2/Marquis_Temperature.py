"""
Author: Shaun Marquis

Purpose: Temperature Calculator - Convert fahrenheit to Celsius
"""

#Get the temperature from the user and store in a variable
fahrenheit = float(input('\nWhat is the temperature in Fahrenheit? '))

#Math to convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

#Output the temperature in Celsius
print(f'The temperature in Celsius is {celsius:.1f} degrees.\n')