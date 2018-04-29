from datetime import date
from datetime import timedelta

# current_date = date(2018,1,1)
# #current_date = date.today()
# print(current_date)
# year = current_date.year
# print(year)
# month = current_date.month
# print(month)
# day = current_date.day
# print(day)
#
unit = timedelta(1)

current_date = date(2018,1,1)
#current_date = date.today()
print(current_date)
current_date -= unit
print(current_date)
current_date += unit
print(current_date)

#Return the day of the week as an integer, where Monday is 0 and Sunday is 6. For example,
# print(current_date.weekday())
