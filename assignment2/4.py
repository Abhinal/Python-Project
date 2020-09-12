# Write a program which takes temperature as input and also input its
#type (Centigrade or Fahrenheit). Convert it to other format.

# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year


temperature = float(input("Enter temperature value: "))
unit = input("\N{DEGREE SIGN}C / \N{DEGREE SIGN}F: ")
if unit == ('c' or 'C'):
    value = (temperature*9)/5 + 32
    print(temperature,u"\N{DEGREE SIGN}C is equal to",value,u"\N{DEGREE SIGN}F")
elif unit == ('f' or 'F'):
    value = (temperature - 32) * (5 / 9)
    print(temperature, u"\N{DEGREE SIGN}F is equal to", value, u"\N{DEGREE SIGN}C")
else:
    print('Error')
