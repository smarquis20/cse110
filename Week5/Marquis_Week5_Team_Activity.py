"""
Author: Shaun Marquis

Purpose: Week 5 team activity List of Numbers
"""

print("Enter a list of numbers, type 0 when finished:")

num_series = []
num = None
total_number = 0
avg_number = 0
largest_num = 0
smallest_num = 1000000000000

while num != 0:
    num = int(input("Enter Number: "))

    if num != 0:
        num_series.append(num)

print()

for i in range(len(num_series)):
    total_number += num_series[i]

    if largest_num < num_series[i]:
        largest_num = num_series[i]
    
    if smallest_num > num_series[i] and num_series[i] > 0:
        smallest_num = num_series[i]

avg_number = total_number / len(num_series)

sort_list = sorted(num_series)

print(f'The sum is: {total_number}')
print(f'The average is: {avg_number}')
print(f'The largest number is: {largest_num}')
print(f'The smallest positive number is: {smallest_num}')
print(f'The sorted list is:')
for i in range(len(sort_list)):
    print(f'{sort_list[i]}')
print()