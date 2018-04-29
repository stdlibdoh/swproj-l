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
from datetime import timedelta

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

    end_date = date.today()
    d = date(2010,1,1)
    unit = timedelta(1)

    #retailers
    groceryRetailers = ['Tescos',"ASDA","Sainsburys","Waitrose","Morrisons"]
    coffeeRetailers = ["Starbucks Coffee", "Costa Coffee","Caffe Nero","Wild Bean Cafe" ]
    lunchRetailers =["Subway","McDonalds","Pret A Manger", "Greggs","The West Cornwall Pasty Company","Chicken Cottage"]
    pubs_and_clubs = ["The Grand Pub","Fabric Club","Heaven Club","Ministry of Sound Club" "XOYO Club"]
    restaurants = ["Scott's Restaurant", "Restaurant Gordon Ramsay" "Portland Restaurant", "Anglo restaurant", "Pizza Express","Dominos Pizza"]
    untagged = ["Cheam Service Station","Paying back James","Paying back Julie","Red Shop", "Tool Shop","Tool Tec", "Civic Shop"]

    with open(p.name+'.csv', 'w', newline='') as csv_file:
        statement = csv.writer(csv_file, delimiter=',')
        statement.writerow(['Day','Month','Year','Description', 'Category','Value','Balance']);

        holiday = False
        current_year = d.year
        while d < end_date:
            if d.day is 1:
                p.balance += p.month_salary
                statement.writerow([d.day,d.month,d.year,"Rhino Sports salary","General", p.month_salary, p.balance])

            if d.day is 7:
                p.balance -= p.rent
                statement.writerow([d.day,d.month,d.year,"Cubit and West rent","Rent", p.rent, p.balance])

            if d.day is 15:
                gasVar = math.trunc(p.gas * random.uniform(0.7, 1.5))
                elecVar = math.trunc(p.electricity * random.uniform(0.7, 1.5))
                #multiplyer for winter months
                if(d.month == 11 or d.month == 0 or d.month == 1):
                    gasVar = math.trunc(gasVar * random.uniform(1, 2.5))
                    elecVar = math.trunc(elecVar * random.uniform(1, 2.5))
                p.balance -= elecVar
                statement.writerow([d.day,d.month,d.year,"BRGAS-Electricity","Bills",elecVar, p.balance])
                p.balance -= gasVar
                statement.writerow([d.day,d.month,d.year,"BRGAS-Gas","Bills",gasVar, p.balance])

            if d.day is 16:
                p.balance -= p.council_tax
                statement.writerow([d.day,d.month,d.year,"LBS Council Tax","Bills",p.council_tax, p.balance])

            if d.day is 20:
                internetVar = math.trunc(p.internet * random.uniform(0.7, 1.5))
                p.balance -= internetVar
                statement.writerow([d.day,d.month,d.year,"VIRGIN MEDIA PYMTS","Bills",internetVar, p.balance])

            if d.day is 24:
                phoneVar = math.trunc(p.phone_bill * random.uniform(1, 1.3))
                p.balance -= phoneVar
                statement.writerow([d.day,d.month,d.year,"O2","Bills",phoneVar, p.balance])

            #weekly shop on thursdays
            if d.weekday() is 4:
                 weekShop = math.trunc(p.grocery *random.uniform(0.7,1.5))
                 p.balance -= weekShop
                 statement.writerow([d.day,d.month,d.year,random.choice(groceryRetailers),"Groceries",weekShop,p.balance])

            if d.weekday() is 0:
                transport_cost = math.trunc(p.transport * random.uniform(0.8,1.3))
                p.balance -= transport_cost
                statement.writerow([d.day,d.month,d.year,"South West Trains","Transport",transport_cost,p.balance])


            #coffee only on weekdays
            if d.weekday() < 5:
                if random.randrange(100) > 20:
                    coffee = math.trunc(2*random.uniform(0.7,1.5))
                    p.balance -= coffee
                    statement.writerow([d.day,d.month,d.year,random.choice(coffeeRetailers),"Eating Out", coffee, p.balance])

                #work lunch on weekdays
                if random.randrange(101) > 35:
                    lunch = math.trunc(6*random.uniform(0.7,1.5))
                    p.balance -= lunch
                    statement.writerow([d.day,d.month,d.year,random.choice(lunchRetailers),"Eating Out", lunch, p.balance])

            #club night
            if d.weekday() is 4 or d.weekday() is 5:
                if random.randrange(100) > 80:
                    num_of_drinks = random.randrange(7)
                    club = random.choice(pubs_and_clubs)
                    for i in range(num_of_drinks):
                        cost_of_round = math.trunc(10*random.uniform(0.5,1.7))
                        p.balance -= cost_of_round
                        statement.writerow([d.day,d.month,d.year,club,"Eating Out", cost_of_round, p.balance])

            #dinner out
            if d.weekday() is 4 or d.weekday() is 5 or d.weekday() is 6:
                if random.randrange(100) > 60:
                    dinner = math.trunc(30*random.uniform(0.8,2))
                    p.balance -= dinner
                    statement.writerow([d.day,d.month,d.year,random.choice(restaurants),"Eating Out", dinner, p.balance])

            #cash withdrawal
            if random.randrange(100) > 70:
                cash_amount = math.trunc(1*random.uniform(1,3))*10
                p.balance -= cash_amount
                statement.writerow([d.day,d.month,d.year,"ATM Cash Withdrawal","General", cash_amount, p.balance])

            #holiday
            if d.month > 5 and d.month < 9 and holiday == False:
                if random.randrange(100) > 90:
                    holiday = True
                    flights = math.trunc(150*random.uniform(0.5,1.5))
                    p.balance -= flights
                    statement.writerow([d.day,d.month,d.year,"British Airways","General", flights, p.balance])

            #untagged elements
            if random.randrange(100)>85:
                untaggedItem = math.trunc(1*random.uniform(1,10))
                p.balance -= untaggedItem
                statement.writerow([d.day,d.month,d.year,random.choice(untagged),"", untaggedItem, p.balance])

            #reset holiday each year
            if holiday == True:
                if d.year>current_year:
                    holiday == False

            #random small shop
            d += unit


class Person:
    def __init__(self, name, rent, transport, grocery, gas, electricity, council_tax, internet, month_salary, phone_bill):
        self.name = name
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

def extractBalance(csv_path, p):
    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile)
        with open(p.name+"_ml.csv",'w',newline='') as ML_CSV:
            writer = csv.writer(ML_CSV, delimiter=',')

            # for row in reader:
            #     writer.writerow([row[-1]])

            firstLine = True
            current_date = date(2010,1,1)
            previous_date = date(2010,1,2)
            previous_row = None

            counter = 0
            for row in reader:
                if firstLine:
                    firstLine = False
                else:
                    current_date = date(int(row[2]),int(row[1]),int(row[0]))
                    if current_date != previous_date:
                        difference_in_dates = current_date-previous_date
                        difference_in_days = timedelta(difference_in_dates.days)
                        for i in range(0,difference_in_days.days-1):
                            writer.writerow([previous_row])

                        previous_date = date(int(row[2]),int(row[1]),int(row[0]))
                        previous_row = row[-1]
                        writer.writerow([row[-1]])


    return "/tmp/ML_CSV.csv"


def main():
    person1 = Person("person_a", 400,20,50,20,20,20,20,1600,20)
    person2 = Person("person_b",440,30,55,25,25,35,30,1600,25)
    person3 = Person("person_c",550,30,60,30,30,50,40,1700,30)
    # person3 = Person("person_c",700,40,80,40,40,70,50,1800,60)
    # expensereport()
    #disposableincome()
    statementGen(person1)
    statementGen(person2)
    statementGen(person3)

    extractBalance("person_a.csv",person1)
    extractBalance("person_b.csv",person2)
    extractBalance("person_c.csv",person3)

    #statementGen(660,92,60,30, 50, 40,1700)

main()



# for i in range(0,len(data)-1):
#     for j in range(0,len(data[i]-1)):
