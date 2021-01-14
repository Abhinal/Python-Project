import calendar

year = int(input("Enter Year: "))
try:
    month = int(input("Enter Month (1,2,3...,12) or leave it blank: "))
    print (calendar.month(year, month))
except:
    print (calendar.calendar(year))
