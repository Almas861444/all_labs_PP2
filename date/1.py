#1
from datetime import date, timedelta
current = date.today() - timedelta(5)
print("Current time: ", date.today())
print("Subtract five days: ", current)

#2
from datetime import datetime, timedelta
time = datetime.now() - timedelta(1)
yesterday = time.strftime("%d-%m-%Y")
print("Yesterday: ", yesterday)

time = datetime.now()
today = time.strftime("%d-%m-%Y")
print("Today: ", today)

time = datetime.now() + timedelta(1)
tomorrow = time.strftime("%d-%m-%Y")
print("Tomorrow: ", tomorrow)

#3
from datetime import datetime, timedelta
time = datetime.now()
del_milseconds = time.strftime("%d-%m-%Y, %H:%M:%S")
print(del_milseconds)

#4
from datetime import datetime, timedelta
yesterday = datetime.now() - timedelta(1)
tomorrow = datetime.now() + timedelta(1)

yesterday = datetime.timestamp(yesterday)
tomorrow = datetime.timestamp(tomorrow)
print(tomorrow - yesterday)