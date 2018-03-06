# Replace lists as dictionary to add days to months
# Need to add an income tag

import csv
import random
import math

def expensesreport():
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

def main():
    expensesreport()

main()