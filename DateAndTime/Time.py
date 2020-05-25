import datetime

#different ways to construct time object
time_1=datetime.time()
print("time_1 =",time_1)

time_2=datetime.time(7,24,50)
print("time_2 =",time_2)

#last argument is microsecond
time_3=datetime.time(7,24,50,10000)
print("time_3=",time_3)

print("hour =", time_3.hour)
print("minute =", time_3.minute)
print("second =", time_3.second)
print("microsecond =", time_3.microsecond)

day_time =datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", day_time.year)
print("month =", day_time.month)
print("hour =", day_time.hour)
print("minute =", day_time.minute)
print("timestamp =", day_time.timestamp())

#used to change date format
now=datetime.datetime.now()

s1=now.strftime("%m/%d/%Y, %H:%M:%S")
print("s1:", s1)

s2=now.strftime("%d/%m/%Y, %H:%M:%S")
print("s2:", s2)

#differnce between 2 date/time

t1=datetime.timedelta(weeks=2,days=5,hours=1,seconds=33)
t2=datetime.timedelta(days=4,hours=11,minutes=4,seconds=54)
print(t1-t2)
print(t2-t1)#negative
print(abs(t2-t1))#converting to postive
