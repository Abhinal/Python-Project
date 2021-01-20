f1 = open("demofile.txt",'r')
f2 = open("demofile10.txt",'a')

data = f1.readlines()

contents = []
for line in data:
    for alpha in line:
        f2.write(alpha)

f2 = open("demofile10.txt", "r")
print("New file have:\n"+f2.read())

f1.close()
f2.close()