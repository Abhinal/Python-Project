def switch(x):
    return switch_case.get(x, default)()
def addition():
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    return(int(a+b))
def subtraction():
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    return(int(a-b))
def multiplication():
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    return(int(a*b))
def division():
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    return(float(a)/float(b))
def exponentiation():
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    return(int(a**b))
def end():
    exit('Good Bye')
def default():
    return "Invalid Season!"

switch_case = {
    1: addition,
    2: subtraction,
    3: multiplication,
    4: division,
    5: exponentiation,
    6: end
}

while True:
    choice = int(input("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\nEnter 5 for Exponentiation\nEnter 6 for Exit\nEnter choice: "))
    print(switch(choice))
