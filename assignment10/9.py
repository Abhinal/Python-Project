def factorial(num):
    value = 1
    for i in range(1,num+1):
        value = value * i
    return value

def combination(n,r):
    fac_n = factorial(n)
    fac_r = factorial(r)
    fac_n_minus_r = factorial(n-r)
    return int(fac_n/(fac_n_minus_r * fac_r))

n = int(input('Enter value of n: '))
r = int(input('Enter value of r: '))

print('Combination:',combination(n,r))