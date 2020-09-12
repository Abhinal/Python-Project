hours = int(input('Total no. of hours worked: '))
rate = int(input('Rate per hour: '))
if hours>40:
    print(hours*rate*1.5)
else:
    print(hours*rate)