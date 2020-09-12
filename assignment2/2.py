# Write pay computation to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours (Input: hours and rate).

# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

hours = int(input('Total no. of hours worked: '))
rate = int(input('Rate per hour: '))
if hours>40:
    print(hours*rate*1.5)
else:
    print(hours*rate)