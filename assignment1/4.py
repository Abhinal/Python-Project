# Write a program to prompt the user for principal amount, annual interest, and years. Print total
# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

principal = int(input('Enter Principal Amount: '))
interest = float(input('Enter Annual Interest: '))
years = int(input('Enter total nos of years: '))

total = (principal + float(((principal * interest)/100)*years))

print("Total Amount is",total)