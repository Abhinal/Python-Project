f1 = open("demofile.txt",'r')
f2 = open("demofile12.txt",'r')
f3 = open("demofile13.txt",'a')

f3.write(f1.read())
f3.write(f2.read())

f3 = open("demofile13.txt",'r')
print("New file:\n"+f3.read())