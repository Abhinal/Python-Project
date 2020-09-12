# Write a program which takes two integers as input. Print whether the
# two numbers are equal, less than, or greater than the other.

# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
if (a==b):
    print ('%d = %d' %(a, b))
elif a>b:
    print ('%d > %d' %(a, b))
else:
    print('%d < %d' %(a, b))