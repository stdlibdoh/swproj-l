import csv
from datetime import date
from datetime import timedelta


for i in range(1,7):
    counter = 0
    with open('statement.csv', "r") as csvfile:
        csv_as_list = reversed(list(csv.reader(csvfile)))
        with open(str(i)+'.csv','w', newline='') as month_csv:
            end_month = 0
            month = 0
            counter = 0
            writer = csv.writer(month_csv, delimiter=',')
            for row in csv_as_list:
                # on first iteration set values
                if month == 0:
                    month = int(row[1])
                    end_month = (month - i) % 12
                    if end_month == 0:
                        end_month = 12


                # if month changed increment counter
                if month != int(row[1]):
                    month = int(row[1])
                    counter += 1
                #stop at end month
                if month == end_month:
                    break
                else:
                    if counter+1 == i:
                        writer.writerow(row)
