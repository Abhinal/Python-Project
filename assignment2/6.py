# Write a program which takes input of a number and check whether it
# is even or odd.

# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

try:

a = int(input('Enter number: '))

if (a==0):
    print ('%d is neither odd nor even' %(a))
elif a%2==0:
    print ('%d is even' %(a))
else:
    print('%d is odd' %(a))
    
 except:
    print('Error, please enter numeric input')
    exit(0)
