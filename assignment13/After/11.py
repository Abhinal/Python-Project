f1 = open("demofile.txt",'r')
f2 = open("demofile11.txt",'a')

data = f1.readlines()

contents = []
for line in data:
    for alpha in line:
        if alpha.isupper():
            f2.write(alpha.lower())
        elif alpha.islower():
            f2.write(alpha.upper())
        else:
            f2.write(alpha)

f2 = open("demofile11.txt", "r")
print("New file have:\n"+f2.read())

f1.close()
f2.close()