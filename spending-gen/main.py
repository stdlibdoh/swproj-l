# expensereport related
# Replace lists as dictionary to add days to months
# Need to add an income tag

# disposableincome related
# it's shite
# Groceries, rent, transport, bills, shopping, eating out, general, income

import csv
import random
import math

def expensereport():
    monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    categorylist = ['Groceries', 'Rent', 'Transport', 'Bills', 'Shopping', 'Eating Out', 'General']
    year = 2017
    rent = 1300
    transport = 92
    grocery_base = 130
    bills_base = 120
    with open('expenses.csv', 'w', newline='') as csv_file:
        expensereport = csv.writer(csv_file, delimiter=',')
        expensereport.writerow(['Year', 'Month', 'Category', 'Value']);
        while year > 2010:
            for month in monthlist:
                grocery = math.trunc(grocery_base * random.uniform(0.7, 1.5))
                bills = math.trunc(bills_base * random.uniform(0.7, 1.5))
                shopping = random.randrange(50)
                eating_out = random.randrange(80)
                general = random.randrange(30)
                for category in categorylist:
                    if category is 'Groceries':
                        value = grocery
                    elif category is 'Rent':
                        value = rent
                    elif category is 'Transport':
                        value = transport
                    elif category is 'Bills':
                        value = bills
                    elif category is 'Shopping':
                        value = shopping
                    elif category is 'Eating Out':
                        value = eating_out
                    elif category is 'General':
                        value = general
                    expensereport.writerow([year, month, category, value])
            year -= 1

def disposableincome():
    with open('disposable.csv', 'w', newline='') as csv_file:
        disposableincome = csv.writer(csv_file, delimiter=',')
        # disposableincome.writerow(['Test', 'Test1', 'Test2'])
        monthlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        rent = 1300                                                             # taken
        transport = 92                                                          # taken
        grocery_base = 130                                                      # n/a
        bills_base = 120                                                        # n/a
        for month in monthlength:
            incomeleft = 2163                                                   # n/a
            grocery = math.trunc(grocery_base * random.uniform(0.7, 1.5))       # taken
            bills = math.trunc(bills_base * random.uniform(0.7, 1.5))           # taken
            shopping = random.randrange(50)
            eating_out = random.randrange(80)
            general = random.randrange(30)
            # tys_eating_number = random.randint(5)
            # tys_eating = ()
            # tys_general = ()
            # tys_shopping = ()
            for i in range(1, month+1):
                if i is 26:
                    incomeleft -= rent
                if i is 7:
                    incomeleft = incomeleft - (2*bills // 3)
                if i is 21:
                    incomeleft = incomeleft - (bills // 3)
                if i is 7:
                    incomeleft = incomeleft - transport
                if i%6 == 0:
                    incomeleft = incomeleft - grocery // 4
                disposableincome.writerow([incomeleft])


def main():
    # expensereport()
    disposableincome()

main()