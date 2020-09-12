# Write a program which takes three numbers as input find maximum of
# three and minimum of the three.

# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

def max_and_min(a, b, c):

    if (a>=b and a>=c):
        print(a,'is maximum of three')
        if (b<=c):
            print(b,'is minimum of three')
    else:
        a,b,c=b,c,a
        max_and_min(a,b,c)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))

max_and_min(a,b,c)

