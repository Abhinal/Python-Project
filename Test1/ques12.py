import datetime

first_name = input('Enter first Name: ')
last_name = input('Enter last Name: ')
dob = input('Enter date of Birth (DDMMYYYY): ')

try:
    date = int(dob[:2])
    month = int(dob[2:4])
    year = int(dob[4:])
    newDate = datetime.datetime(year, month, date)
    print(f'Hi {first_name} {last_name}!Your DOB is {date}/{month}/{year}.')
except:
    print(f'Date is wrong')
