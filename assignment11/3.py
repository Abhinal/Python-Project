import datetime

now = datetime.datetime.now()

print("Year: ", datetime.date.today().strftime("%Y"))
print("Month: ", datetime.date.today().strftime("%m"))
print("Day: ", datetime.date.today().strftime("%d"))
print("Current time: ",datetime.datetime.now().time())
print("Current date and time: ",datetime.datetime.now())