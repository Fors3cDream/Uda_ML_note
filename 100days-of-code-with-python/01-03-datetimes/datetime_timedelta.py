"""
Create by Killer at 2019-05-15 17:15
"""

from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

print(t.days)
print(t.seconds)
#print(t.hours)
print(t.seconds/60/60)
print(t.seconds/3600)


eta = timedelta(hours=7)

today = datetime.today()

print(today+eta)