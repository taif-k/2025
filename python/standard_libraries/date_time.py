import datetime

# to get current date & time
todaydate = datetime.datetime.now()
print(todaydate)

# to get previous or future date and time
tomorrowdate = todaydate + datetime.timedelta(1,0,0,0,0,1)
print(tomorrowdate)

previousdate = todaydate + datetime.timedelta(-1) # or todaydate - dt.timedelta(1)
print(previousdate)

# to get specific date & time
year = int(input("Enter year"))
month = int(input("Enter month"))
day = int(input("Enter day"))
specific_date = datetime.datetime(year,month,day) # dt.datetime(2025,4,6)
print(specific_date)



