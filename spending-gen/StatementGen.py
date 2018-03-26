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
from datetime import date

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

def statementGen(p):
    monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    categorylist = ['Groceries', 'Rent', 'Transport', 'Bills', 'Shopping', 'Eating Out', 'General']
    monthlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = date.today().year


    #balance = 0
    groceryRetailers = ['Tescos',"ASDA","Sainsburys","Waitrose","Morrisons"]

    with open('statement.csv', 'w', newline='') as csv_file:
        statement = csv.writer(csv_file, delimiter=',')
        statement.writerow(['Day','Month','Year','Description', 'Category','Value','Balance']);

        #year
        while year > 2010:
            #month
            for month in range(0,12,1):
                #day
                for i in range(1,monthlength[month]+1):
                    #bills
                    if i is 1:
                        p.balance += p.month_salary
                        statement.writerow([i,monthlist[month],year,"Rhino Sports salary","General", p.month_salary, p.balance])

                    if i is 7:
                        p.balance -= p.rent
                        statement.writerow([i,monthlist[month],year,"Cubit and West rent","Rent", p.rent, p.balance])

                    if i is 15:
                        gasVar = math.trunc(p.gas * random.uniform(0.7, 1.5))
                        elecVar = math.trunc(p.electricity * random.uniform(0.7, 1.5))
                        #multiplyer for winter months
                        if(month == 11 or month == 0 or month == 1):
                            gasVar = math.trunc(gasVar * random.uniform(1, 2.5))
                            elecVar = math.trunc(elecVar * random.uniform(1, 2.5))
                        p.balance -= elecVar
                        statement.writerow([i,monthlist[month],year,"BRGAS-Electricity","Bills",elecVar, p.balance])
                        p.balance -= gasVar
                        statement.writerow([i,monthlist[month],year,"BRGAS-Gas","Bills",gasVar, p.balance])

                    if i is 16:
                        p.balance -= p.council_tax
                        statement.writerow([i,monthlist[month],year,"LBS Council Tax","Bills",p.council_tax, p.balance])

                    if i is 20:
                        internetVar = math.trunc(p.internet * random.uniform(0.7, 1.5))
                        p.balance -= internetVar
                        statement.writerow([i,monthlist[month],year,"VIRGIN MEDIA PYMTS","Bills",internetVar, p.balance])

                    if i is 24:
                        phoneVar = math.trunc(p.phone_bill * random.uniform(1, 1.3))
                        p.balance -= phoneVar
                        statement.writerow([i,monthlist[month],year,"02","Bills",phoneVar, p.balance])

                    #weekly shop
                    if i%7 is 4:
                        weekShop = math.trunc(p.grocery *random.uniform(0.7,1.5))
                        p.balance -= weekShop
                        statement.writerow([i,monthlist[month],year,random.choice(groceryRetailers),"Groceries",weekShop,p.balance])
                    #random small shop
                    if 








            print(year)
            year -= 1
class Person:
    def __init__(self, rent, transport, grocery, gas, electricity, council_tax, internet, month_salary, phone_bill):
        self.rent = rent
        self.transport = transport
        self.grocery = grocery
        self.gas = gas
        self.electricity = electricity
        self.council_tax = council_tax
        self.internet = internet
        self.month_salary = month_salary
        self.balance = 0
        self.phone_bill = phone_bill



def main():
    person1 = Person(660,30,60,30,30,50,40,1700,30)
    # expensereport()
    #disposableincome()
    statementGen(person1)

    #statementGen(660,92,60,30, 50, 40,1700)

main()
