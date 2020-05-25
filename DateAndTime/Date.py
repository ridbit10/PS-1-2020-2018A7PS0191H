import datetime

#gets current date and time
datetime_object=datetime.datetime.now()
print(datetime_object)

#gets todays date
date_object=datetime.date.today()
print(date_object)

#date is a constructor
d=datetime.date(1999,10,6)
print(d)

#date from timestamp
timestamp=datetime.date.fromtimestamp(1326244364)
print("Date =",timestamp)

today =datetime.date.today()
print("Year is",today.year)
print("Month is",today.month)
print("Day is",today.day)

#different ways to construct time object
time_1=datetime.time()
print("time_1 =",time_1)

time_2=datetime.time(7,24,50)
print("time_2 =",time_2)

#last argument is microsecond
time_3=datetime.time(7,24,50,10000)
print("time_3=",time_3)
