"""
Author: Shaun Marquis

Purpose: Opens flu csv and analyzes the data
"""
#For extra credit i added a check to identify the year and country that has the largest drop from one year to the next.  It will list
#the country, drop difference, and the previous and current year of the max drop.

#initalize variables
max_year = 0
min_year = 10000
max_country = ""
min_country = ""
min_life_expec = 10000
max_life_expec = 0
sum_life_expec = 0
life_expec_len = 0
user_max_life = 0
user_min_life = 10000
user_min_country = ""
user_max_country = ""
max_drop = 0
max_drop_country = ""
max_drop_year = 0
previous_life = 0
previous_country = ""

#Get user year input
user_year = int(input("\nEnter the year of interest: "))

#open flu data csv and assign to variable
with open("life-expectancy.csv") as flu_data:
    next(flu_data)

    #for loop to pull each row and assign each to a variable
    for data in flu_data:
        clean_line = data.strip()
        csv = clean_line.split(",")

        country = csv[0]
        country_code = csv[1]
        year = int(csv[2])
        life_expec = float(csv[3])

        current_expec = 0

        #extra credit - Check to make sure largest drop check is between the same country
        if country == previous_country:
            if previous_life == 0:
                previous_life = life_expec

            #Subtracts the current life expectancy with the previous and if currently the largest will be set to max variable
            else:
                current_expec = previous_life - life_expec
                if current_expec > max_drop:
                    max_drop = current_expec
                    max_drop_country = country
                    max_drop_year = year
                    max_prev_year = previous_year
                
        #This is how i skip the first row for each country to keep the math correct for max drop
        else:
            previous_life = 0
            previous_country = country

        previous_country = country
        previous_year = year
        previous_life = life_expec

        #sets max life expectancy for entire data set
        if life_expec > max_life_expec:
            max_year = year
            max_country = country
            max_life_expec = life_expec

        #sets min life expectancy for entire data set
        if life_expec < min_life_expec:
            min_year = year
            min_country = country
            min_life_expec = life_expec
        
        #takes the users year and sums all life expectancies for that year and counts the number of rows
        if user_year == year:
            life_expec_len += 1
            sum_life_expec += life_expec

            #sets the max life expectancy and country for the year selected
            if life_expec > user_max_life:
                user_max_country = country
                user_max_life = life_expec

            #sets the min life expectancy and country for the year selected
            if life_expec < user_min_life:
                user_min_country = country
                user_min_life = life_expec

    #prints overall max and min life expectancy, country, and year
    print(f"\nThe overall max life expectancy is: {max_life_expec} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min_life_expec} from {min_country} in {min_year}")
    print(f"{max_drop_country} had the largest drop of life expectancy from the previous year with {max_drop:.2f} between {max_prev_year} and {max_drop_year}.")

    #prints user select year life expectancy, country, and year
    print(f"\nFor the year {user_year}:")
    print(f"The average life expectancy across all countries was {sum_life_expec / life_expec_len:.2f}")
    print(f"The max life expectancy was in {user_max_country} with {user_max_life}")
    print(f"The min life expectancy was in {user_min_country} with {user_min_life}")
    print()
