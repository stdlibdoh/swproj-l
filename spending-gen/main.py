# expensereport related
# Replace lists as dictionary to add days to months
# Need to add an income tag

# disposableincome related
# Groceries, rent, transport, bills, shopping, eating out, general, income
# can't believe i forgot a pen
# random number between 0 and 10
# 0-4 -> no change
# 4-6 -> shopping
# 6-9 -> eating_out
# 9-10 -> general

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
        monthlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        incomeleft = 0
        monthsalary = 1700                                                      # added
        rent = 1300                                                             # expended
        transport = 92                                                          # expensed
        grocery_base = 130                                                      # n/a
        bills_base = 120                                                        # n/a
        for month in monthlength:
            incomeleft += monthsalary                                           # n/a
            grocery = math.trunc(grocery_base * random.uniform(0.7, 1.5))       # expensed
            bills = math.trunc(bills_base * random.uniform(0.7, 1.5))           # expensed
            shopping = random.randrange(300)                                    # expensed
            eating_out = random.randrange(200)                                  # expensed
            general = random.randrange(70)                                      # expensed
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
                tys_mod = random.randint(0, 10)
                if tys_mod >= 0 & tys_mod < 4:
                    # no change
                    incomeleft = incomeleft
                elif tys_mod >= 4 & tys_mod < 6:
                    # shopping charge
                    incomeleft -= shopping
                elif tys_mod >= 6 & tys_mod < 9:
                    # eating out charge
                    incomeleft -= eating_out
                elif tys_mod >= 9 & tys_mod <= 10:
                    # general charge
                    incomeleft -= general
                disposableincome.writerow([incomeleft])


def main():
    # expensereport()
    disposableincome()

main()
