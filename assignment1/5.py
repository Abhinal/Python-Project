# Write a program in Python to find the root of a quadratic equation taken as input.
# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b*b - 4*a*c) ** (1/2)

first = (-b + d)/2*a
second = (-b - d)/2*a

print("The root of quadratic equation are",first,"and",second)