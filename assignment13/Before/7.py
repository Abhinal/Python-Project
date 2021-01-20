words = []
f = open("demofile7.txt","r")

for line in f:
    w=line.split()
    words.append(len(w))
print(max(words))