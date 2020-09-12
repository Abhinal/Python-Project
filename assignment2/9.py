# Write a program to check whether a number is Armstrong or not.

# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

number = int(input('Enter a number: '))
temp = number
sum = 0
while(temp > 0):
    sum = sum + (temp%10)**3
    temp = int(temp/10)

if number == sum:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')