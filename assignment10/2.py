def pascalTriangle(n):
    for i in range(0, n):
        coff = 1
        for j in range(0, n-i):
            print(end="  ")  
        for k in range(0, i+1):
            print(coff, end="   ")
            coff = int(coff * (i - k) / (k + 1))
        print('\n')

n = int(input("Enter the number of rows: "))
pascalTriangle(n)