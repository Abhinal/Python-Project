# Write pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

try:
    hours = int(input('Enter Hours: '))
except:
    print('Error, please enter numeric input')
    exit(0)
try:
    rate = int(input('Rate per hour: '))
except:
    print('Error, please enter numeric input')
    exit(0)