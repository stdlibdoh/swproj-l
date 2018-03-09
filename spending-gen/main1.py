import csv
import random
import math

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
    disposableincome()

main()
