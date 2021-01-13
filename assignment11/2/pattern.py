def pypart(n=5):
    for i in range(0, n):
        print("* " * (i+1))

def pypart2(n):
    k = 2*n - 2
    for i in range(0, n):
        for _ in range(0, k):
            print(end=" ")
        k = k - 2
        for _ in range(0, i+1):
            print("* ", end="")
        print("\r")

def triangle(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r") 

def numpat(n): 
    num = 1
    for i in range(0, n):
        num = 1
        for _ in range(0, i+1):
            print(num, end=" ")
            num += 1
        print("\r") 

def countnum(n): 
    num = 1
    for i in range(0, n):
        for _ in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r") 
