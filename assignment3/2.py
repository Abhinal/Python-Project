# Write a program to find whether a number is prime or not.

while True:
    try:
        n = int(input("Enter a number: "))
        break
    except:
        print("Invalid Response")
if n > 1:
    for i in range(2, n):
        if(n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")