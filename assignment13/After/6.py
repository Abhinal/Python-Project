words = 0
f = open("demofile.txt","r")

for line in f:
    w=line.split()
    words+=len(w)
max_len=len(max(w,key=len))
print(words)