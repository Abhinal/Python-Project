def refibo(n):
   if n <= 1:
       return n
   else:
       return(refibo(n-1) + refibo(n-2))

def fibo(n):
    n1, n2 = 0, 1
    count = 0
    while count < n:
       print(n1,end='  ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
    print('\n')

n = int(input("Enter n to print Fibonacci Series: "))

choice = input('Enter 1 for recursive function\nEnter 2 for non-recursive function\nChoice: ')

print("Fibonacci series:",end=' ')
if choice == '1':
    for i in range(n):
        print(refibo(i),end='  ')
    print('\n')
elif choice == '2':
    fibo(n)
else: print('Invalid Choice')