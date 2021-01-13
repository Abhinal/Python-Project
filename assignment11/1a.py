def leapYear(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return f"{year} is a Leap Year"
    else: return f"{year} is not a Leap Year"


print(leapYear(int(input("Enter year: "))))