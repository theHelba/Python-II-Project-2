#Chris Harley
#09/26/2024
#PROG 1403 - Programming Logic II
#currency_manager.py - Manages the currency collection and conversion logic.

import csv
from urllib.request import urlopen

def loadCurrencies(url):
    '''Load the currencies from a CSV file at the given URL
       Returns a dictionary where each key maps to a list of currency data.
    '''
    currencies = {}

    try:
        file = urlopen(url)
        csvReader = csv.reader(file.read().decode('utf-8').splitlines())
        #skips header
        next(csvReader)
        for row in csvReader:
            #gives row 4 columns (country, currency, code, rate)
            if len(row) >= 4:
                country = row[0].strip()
                currency = row[1].strip()
                code = row[2].strip()
                try:
                    rate = float(row[3].strip())  #converts rate to float
                except ValueError:
                    print(f"Invalid rate for currency: {row}")
                    continue
                
                #appends data to a list
                def addToDict(key, data):
                    key = key.lower()
                    if key not in currencies:
                        currencies[key] = []
                    currencies[key].append(data)

                #stores information, allows multiple entries for the same currency/code(resolves issues of overwriting)
                currencyData = {'country': country, 'currency': currency, 'code': code, 'rate': rate}
                addToDict(country, currencyData)
                addToDict(currency, currencyData)
                addToDict(code, currencyData)
                
        return currencies

    except Exception as e:
        print(f"Error loading currencies: {e}")
        return None


def convertCurrency(amount, currencyType, currencies):
    '''Convert user amount based on the currency type and display the conversion
       amount (float): The amount to be converted
       currencyType (str): The type of currency (country, currency, code)
       currencies (dict): A dictionary of currency data
    '''
    currencyType = currencyType.lower()

    if currencyType in currencies:
        currencyList = currencies[currencyType]  #creates a list of matches
        print(f"Converting {amount} to the following currencies :")
        
        for currencyData in currencyList:
            currencyRate = currencyData.get('rate', None)      
            currencyName = currencyData.get('currency', '')
            currencyCode = currencyData.get('code', '')
            countryName = currencyData.get('country', '')
            
            if currencyRate is not None:
                convertedValue = round(amount * currencyRate, 2)  #rounds converted value to 2 decimal places
                print(f"{countryName} rate of {currencyRate} is {convertedValue:.2f} {currencyName} ({currencyCode})")
            else:
                print(f"Exchange rate not found for currency type: {currencyType}")
    else:
        print(f"Currency '{currencyType}' not found. Please try again.")