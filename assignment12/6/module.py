# F(x,y)=F(x-y,y)+1
def a(x, y):
    if y > x:
        return 0
    return a(x-y, y) + 1

# F(n,r)=F(n-1,r)+F(n-1,r-1)
def b(n, r):
    if n == 1 or r ==1:
        return 1
    return b(n-1, r) + b(n-1, r-1)

# F(n)=F(n/2)+1
def c(n, dummy):
    if n <= 1:
        return 0
    return c(n//2, 1) + 1
    
# F(M,N)=F(M-1,N)+F(M-1,N-1)
def d(m,n):
    if m == 0 or (m >= n and n>= 1):
        return 1
    return d(m-1, n) + d(m-1, n-1)


# B(m,x)=m!/(x!(m-x)!) where m&gt;x,    B(0,0)=B(m,0)=1 and B(m,x)=B(m,x-1)*[(m-x+1)/x]
def fact(n):
    if n <= 0:
        return 1
    return n * fact(n-1)

def e(m, x):
    if m < x:
        return -1
    return fact(m)//(fact(x)*fact(m-x))
