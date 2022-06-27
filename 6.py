# Importing Module 
import sys
from datetime import datetime
from datetime import time
from datetime import date
#Question 1 Revise code to current time
def main():
    dt = datetime.now()
    time_string = dt.strftime("%X")
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        _date, _time, store, item, cost, payment = data
        print("{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}")
main()

#Question 2
from datetime import timedelta
current_time = datetime.now()
print(currenttime.strftime("%H:%M:%S"))
#Subtract 60 seconds
time = current - datetime.timedelta(seconds=60)
print(time.strftime("%H:%M:%S"))
#Adding 1 year
next_year = current_time.replace(year=today.year+1).strftime("%Y.%m.%d")
print(next_year)
#Adding 1 more year 
two_year = next_year.replace(year=today.year+1).strftime("%Y.%m.%d")

#Question 3
d = timedelta(days = 100, hours = 10, minutes = 13)
print(d)

#Question 4
# current date 
datetime_object = datetime.now
print(datetime_object)
print('Type :-',type(datetime_object))
#converting feet to inches
feet = int(input())
def convert()
    inches = feet*12
    print(inches)
convert(feet)
