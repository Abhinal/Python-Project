#Divide two numbers truncating the fractional part. Input the two numbers.
# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = math.trunc(a/b)
print(a,"/",b,"=",c)