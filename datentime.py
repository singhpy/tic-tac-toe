import datetime
import time
import calendar
"""
    naive - 
    aware - 
    (year, month, day, hour, minute, second, microsecond)
    
    timedelta = Only days, seconds and microseconds are stored internally. Arguments are converted to those units
    timedelta = you can use total_seconds() to calculate duration in only seconds
    
    date = methods are - today(), replace(), weekday(), isoweekday(), isocalendar(), isoformat(), __str__(), 
                         ctime(), strftime(format), __format__(format), 
    
    

# module attributes

print("Module Attributes are MIN & MAX  " + str(datetime.MINYEAR) + "   " + str(datetime.MAXYEAR))

# available types  - date, time, datetime, timedelta, tzinfo

type_date = datetime.date(2017, 12, 25)     # naive
type_time = datetime.time(10, 58, 59, 599, None)     # naive ( no tzinfo)
type_datetime = datetime.datetime(2018, 12, 25, 10, 58, 59, 599, None)     # naive ( no tzinfo)
    # (year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
type_timedelta = datetime.timedelta(1, 10, 1000, 100, 10, 100, 2)   # days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0
type_timedelta_good_practice = datetime.timedelta(days=1, seconds=10, microseconds=1000, milliseconds=100, weeks=10,
                                                  hours=10, minutes=2)
#type_tzinfo = datetime.tzinfo()
#type_timezone = datetime.timezone()

print( "Available types are {} {} {} {} ".format( type_date, type_datetime, type_time, type_timedelta))
                                                                            #type_tzinfo))

# timedelta class attributes

print("timedelta Attributes are min. max and resolution  " + str(datetime.timedelta.min) + "   " + str(datetime.timedelta.max) + "  " + str(datetime.timedelta.resolution))

# date class attributes/method
# min, max, resolution

type_date_today = datetime.date.today()
print("Today's date {}. Year {}. Month {}. Day {}.".format(type_date_today,type_date_today.year, type_date_today.month, type_date_today.day))

# replace
type_date_replaced = type_date.replace(year=2020)
print( "Replaced output are {} {} ".format( type_date, type_date_replaced))
#  today == date.fromtimestamp(time.time())

# counting days to an event - how many days to my birthday

bday_month = input("Enter your Birthday Month ")
bday_day = input("Enter your Birthday day ")
print("You entered {} {} ".format(bday_month, bday_day))
next_birthday_date = datetime.date(year=2018, month=int(bday_month), day=int(bday_day))
print("Time to Birthday in days {} ".format(abs(next_birthday_date-type_date_today)))

# strftime









"""
# datetime - class attributes - min, max, resolution,
today_datetime = datetime.datetime.today() # tzinfo = None
print("DateTime of today {} ".format(today_datetime))

now_datetime = datetime.datetime.now(tz=None) # tzinfo = None is same as today
print("DateTime of now {} ".format(now_datetime))

timestamp_datetime = datetime.datetime.fromtimestamp(time.time(),tz=None) # tzinfo = None is same as today
print("DateTime of timestamp {} ".format(timestamp_datetime))

utcnow_datetime = datetime.datetime.utcnow()
print("DateTime of utcnow {} ".format(utcnow_datetime))

# now_aware_datetime = datetime.datetime.now(timezone.utc) # tzinfo = None is same as today
# print("DateTime of now aware {} ".format(now_aware_datetime))


# strptime




