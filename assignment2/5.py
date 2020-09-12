# Write a program which takes input of a number and check whether it
# is positive or negative.

# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

a = int(input('Enter number: '))
if (a==0):
    print ('%d is neither positive nor negative' %(a))
elif a>0:
    print ('%d is positive' %(a))
else:
    print('%d is negative' %(a))