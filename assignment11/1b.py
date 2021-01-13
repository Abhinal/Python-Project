COUNT = 0

def leapYear(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        global COUNT
        COUNT += 1


for i in range(1000, 2021):
    leapYear(i)
print(f"Total numbers of leap year between 1000 and 2021 is {COUNT}.")