"""
Author: Shaun Marquis

Purpose: Meal Calculator - Ask user for meal prices and number of people and
calculate and display the subtotal, tax, final price, and change.
"""

#Get the number of adults and children and the prices they paid for their meals
price_child = float(input('\nChilds meal price: '))
price_adult = float(input('Adults meal price: '))
children_number = int(input('Number of children: '))
adult_number = int(input('Number of Adults: '))

#Calculations to get subtotal
sub_total = price_child * children_number + price_adult * adult_number

#Display subtotal
print(f'\nSubtotal: ${sub_total:.2f}\n')

#Get sales tax percentage
percent_tax = float(input('What is the sales tax rate? '))

#Display total after including tax rate to the subtotal
sales_tax = (sub_total * percent_tax) / 100
total = sub_total + sales_tax

print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')

#Ask user for amount paid and calculate change
amount_paid = float(input('\nWhat is the payment amount? '))

change = amount_paid - total

print(f'Change: ${change:.2f}\n')