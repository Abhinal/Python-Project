def switch(x):
    return switch_case.get(x, default)(value, year)
def seniorCitizen(value,year):
    return(value + (value*(0.12)*year))
def normalCitizen(value,year):
    return(value + (value*(0.10)*year))
def default():
    return 'Invalid Session!'

switch_case = {
    'y': seniorCitizen,
    'n': normalCitizen,
}

value = int(input('Enter value: '))
year = int(input('Enter year: '))
choice = (input('Are you a Senior Citizen (y or n)? '))
print(switch(choice))