"""
Author: Shaun Marquis

Purpose: Ask for employee information and display ID card with formatting.
"""
#Grab required input from the user
first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
email = input('Please enter your email: ')
phone_number = input('Please enter your phone number: ')
job_title = input('Please enter your job title: ')
id_number = input('Please enter your ID number: ')
hair_color = input('What color is your hair: ')
eye_color = input('What color are your eyes: ')
work_month = input('What month did you start work here: ')
training = input('Did you complete Advanced Training: ')

#Output data in a formatted card
print()
print('The ID Card is:')
print('------------------------------------------')
#Using formatting strings to force the desired formatting
print(last_name.upper() + ', ' + first_name.capitalize())
print(job_title.title())
print('ID: ' + id_number)
print()
print(email.lower())
print(phone_number)
print(f"{'Hair: ' + hair_color.capitalize():<25} Eyes: {eye_color.capitalize()}")
print(f"{'Month: ' + work_month.capitalize():<25} Training: {training.capitalize()}")
print('------------------------------------------')
print()