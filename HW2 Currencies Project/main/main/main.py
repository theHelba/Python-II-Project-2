#Chris Harley
#09/26/2024
#PROG 1403 - Programming Logic II
#main.py - Currency Converter Project

from user_input import getAmount, getCurrency
from currency_management import loadCurrencies, convertCurrency

def main():
    '''main function loads data from URL (loadCurrencies)
       gets user input (getAmount, getCurrency)
       makes conversion then displays results (convertCurrency)
    '''
    url = 'https://raw.githubusercontent.com/theHelba/September-2024-monthly-exchange-rates/main/exrates-monthly-0924.csv'
    currencies = loadCurrencies(url)
    amount = getAmount()
    currencyType = getCurrency()
    convertCurrency(amount, currencyType, currencies)

if __name__ == "__main__":
    main()

