from module import a, b, c, d, e

print("a) F(x,y)=F(x-y,y)+1, if y ≤ x\nb) F(n,r)=F(n-1,r)+F(n-1,r-1)\nc) F(n)=F(n/2)+1 if n&gt;1\nd) F(M,N)=1 if M=0, or M ≥N ≥1, and F(M,N)=F(M-1,N)+F(M-1,N-1), otherwise.\ne) B(m,x)=m!/(x!(m-x)!) where m&gt;x,\n   B(0,0)=B(m,0)=1 and B(m,x)=B(m,x-1)*[(m-x+1)/x]\n")
while True:
    choice = globals()[input("Type 'a', 'b', 'c', 'd' or 'e' according to question: ")]
    print(choice(int(input("Enter first input: ")), int(input("Enter second number or 1: "))))