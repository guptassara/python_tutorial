import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now_string = now.strftime("%H:%M:%S %d-%m-%y")

print(date)
print(today)
print(time)
print(now)
print(now_string)


target_datetime = datetime.datetime(2000, 4, 15, 12, 22, 9)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")
