#Write a program to print Fibonacci numbers for a range 1 to 1000.

print('Fibonacci Numbers in a range 1 to 1000 are :')
first, second = 0, 1
while second <= 1000:
    print(second)
    first, second = second, first + second
