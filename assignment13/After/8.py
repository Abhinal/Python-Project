f1 = open("demofile.txt",'r')
f2 = open("demofile8.txt",'a')

data = f1.readlines()

contents = []
for line in data:
    contents.append(line)
f1.close()

contents.reverse()
for content in contents:
    f2.write(content[::-1])

f2 = open("demofile8.txt", "r")
print("New file have:\n"+f2.read())
f2.close()