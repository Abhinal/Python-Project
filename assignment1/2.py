# Write a program which takes temperature as input as Centigrade. Convert it to Fahrenheit.
# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

celcius = float(input("Enter temperature value in celcius: "))
fahrenheit = (celcius*9)/5 + 32
print(celcius,u"\N{DEGREE SIGN}C is equal to",fahrenheit,u"\N{DEGREE SIGN}F")