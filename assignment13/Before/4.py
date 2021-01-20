f = open("demofile4.txt",'r')
data = f.readlines()
for line in data:
    word = line.split()
    print(word)
f.close()