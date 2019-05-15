"""
Create by Killer at 2019-05-15 17:02
"""
from datetime import date, datetime

import time

time_now = time.time()
print(time_now)


today = datetime.today() # 2019-05-15 17:04:47.273612

day_now = datetime.now()
print(day_now)

print(type(today))
print(today)

print(day_now == today)

today_date = date.today() # 2019-05-15
print(type(today_date))
print(today_date)

print("Month: ", today_date.month)

print("Year: ", today_date.year)

print("day: ", today_date.day)

christmas = date(2019, 12, 25)
print(christmas)

if christmas is not today_date:
    print("Sorry there are still " + str((christmas - today_date).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")