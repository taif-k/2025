import datetime
import time
import calendar

# to get current date & time
todaydate = datetime.datetime.today()
print(todaydate)
format_date = todaydate.strftime("%d/%m/%Y")
print(format_date)


# to get previous or future date and time
tomorrowdate = todaydate + datetime.timedelta(1,0,0,0,0,1)
print(tomorrowdate)

previousdate = todaydate + datetime.timedelta(-1) # or todaydate - dt.timedelta(1)
print(previousdate)

# to get specific date & time
year = int(input("Enter year"))
month = int(input("Enter month"))
day = int(input("Enter day"))
specific_date = datetime.datetime(year,month,day) # datetime.datetime(2025,4,6)
print(specific_date)

# generate a unique id
data_time = time.time()
name = input("Enter name") + str(data_time)
print(name)

# pause execution, sleep
print("paused for 3 seconds")
time.sleep(3)
print("executed after 3 seconds")


data = calendar.calendar(2025)
print(data)

# print(calendar.month(2025,4))

year = 2025
is_leap = calendar.isleap(year)
print(f"{year} is a leap year: ",is_leap)

month_range = calendar.monthrange(year,4)
print(month_range)

id = int(input("Enter id: "))
count = 0
while count <= 4:
    count = count + 1
    print("Searching.")
    time.sleep(0.5)
    print("Searching..")
    time.sleep(0.5)
    print("Searching...")
    

print("Entered id is ",id)




