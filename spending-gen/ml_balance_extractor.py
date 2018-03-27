import csv
from datetime import date
from datetime import timedelta

def extractBalance():
    with open('statement.csv') as csvfile:
         reader = csv.reader(csvfile)
         with open('test2.csv','w',newline='') as ML_CSV:
             writer = csv.writer(ML_CSV, delimiter=',')
             firstLine = True
             current_date = date(2010,1,1)
             previous_date = date(2010,1,2)
             previous_row = None

             # counter = 0
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

                # counter+=1
                # if counter > 20:
                #     break

def concat(csv1, csv2):
    main = open(csv1,"a")
    for row in open(csv2):
        main.write(row)




extractBalance()
concat("test.csv","test2.csv")
# with open('test.csv','w') as ML_CSV:
#     writer = csv.writer(ML_CSV)
#     for i in range(100):
#         writer.writerow([i])
