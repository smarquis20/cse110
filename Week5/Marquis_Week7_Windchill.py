
"""
Author: Shaun Marquis

Purpose: Calculate temperature with wind chill.
"""

import math

# function to calculate Wind Chill
def wind_chill(temp, wind_speed): 
      
    # Calculating Wind Chill 
    wind_chill = 35.74 + (0.6215 * temp) - 35.75 * (wind_speed ** 0.16) + (0.4275 * temp) * (wind_speed ** 0.16)
    return wind_chill

# function to convert Fahrenheit to Celsius
def convert_degree(orig_temp):
    
    # math to convert Fahrenheit to Celsius
    new_temp = (orig_temp * 9/5) + 32
    return new_temp

# Ask user for temperature and Fahrenheit or Celsius
temp = float(input("What is the temperature? "))
degree_type = input("Fahrenheit or Celsius (F/C)? ")
degree_type = degree_type.upper()
wind_speed_array = [5,10,15,20,25,30,35,40,45,50,55,60]

# If user selects Celsius then convert Fahrenheit
if degree_type == 'C':
    temp = convert_degree(temp)

# For loop to loop through the MPH array and calculate temperature according to MPH
for i in range(len(wind_speed_array)):
    calc_wind = wind_chill(temp, wind_speed_array[i])
    
    # Prints all windchills for each MPH in the array
    print(f"At temperature {temp}F, and wind speed {wind_speed_array[i]} mph, the windchill is: {calc_wind:.2f}F")
