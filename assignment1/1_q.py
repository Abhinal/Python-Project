#Take input of a floating-point number and an integer.
#Multiply them. Add three with the result
#without saving it as a separate variable.
#Also, round it up to two decimal places without
#saving it as a separate variable.
# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

number = float(input('Enter a number: '))
print('Result is {:.2f}'.format(((number+3)*3)+3))