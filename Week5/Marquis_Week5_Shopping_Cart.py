"""
Author: Shaun Marquis

Purpose: Week 5 shopping cart.
"""

print("Welcome to the Shopping Cart Program!")

user_choice = None
shopping_list = []
shopping_price = []
item = None

#Basic user menu
while user_choice != "5":
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    user_choice = (input("Please enter an action: "))

    #Append will add item and price to each list.
    if user_choice == "1" or user_choice.lower() == "add item":
        item = input("What item would you like to add? ")
        shopping_list.append(item)
        price = float(input(f"what is the price of '{item}'? "))
        shopping_price.append(price)
        print(f"'{item}' has been added to the cart.")

    #range will populate index number to list each item in the shopping array and price.
    elif user_choice == "2" or user_choice.lower() == "view cart":
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_list)):
            item_array = shopping_list[i]
            price_array = shopping_price[i]
            print(f"{i+1}. {item_array} - ${price_array}")

    #remove item from the shopping cart.  Subtract 1 from the index to line up with 0-based index.
    elif user_choice == "3" or user_choice.lower() == "remove item":
        item_remove = int(input("Which item would you like to remove? "))
        max_length = len(shopping_list)
    
        if item_remove <= max_length and item_remove >= 1:
            shopping_list.pop(item_remove - 1)
            shopping_price.pop(item_remove - 1)
            print("Item has been removed.")
        else:
            print("Invalid option for removal. Please choose a number from the list.")

    elif user_choice == "4" or user_choice.lower() == "compute total":
        compute_total = 0
        for i in range(len(shopping_price)):
            compute_total += shopping_price[i]
        print(f"The total price of the items in the shopping cart is ${compute_total:.2f}")

    #Will exit the loop and quit the program
    elif user_choice == "5" or user_choice.lower() == "quit":
        print("Thank you. Goodbye.")
        break

    #loop back to top and ask the user to re-enter their choice.
    else:
        print("You must choose 1 - 5.  Please choose again.")