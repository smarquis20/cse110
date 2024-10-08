"""
Author: Shaun Marquis

Purpose: Open files and read from the file
"""

with open("hr_system.txt") as hr_file:

    for i in hr_file:
        file = i.split(" ")
        i.strip

        name = file[0]
        title = file[2]
        id = file[1]
        salary = file[3]

        salary = float(salary)

        #print(f"{name}, Title: {title}")
        print(f"{name} (ID: {id}), {title} - ${salary:.2f}")
