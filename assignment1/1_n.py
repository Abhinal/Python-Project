# Perform string conversion.
# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

a = str(input('Enter a string : '))
print("Before Conversion value is",a)
t = tuple(a)
print("After Conversion from string to tuple value is",t)
l = list(a)
print("After Conversion from string to list value is",l)
s = set(a)
print("After Conversion from string to set value is",s)