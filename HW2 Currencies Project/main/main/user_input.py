#Chris Harley
#09/26/2024
#PROG 1403 - Programming Logic II
#user_input.py - Handles user input for the currency converter.

def getAmount():
    '''get user input for amount
    '''
    while True:
        try:
            amount = float(input("Enter the amount of currency > "))
            if amount > 0:
                return amount
            else:
                print("Enter a positive value")
        except ValueError:
            print("Enter a number")

def getCurrency():
    '''get currency type from user
    '''
    return input("Enter the Country Name, Currency Name, or Currency Code > ").strip().lower()

