print("Before:")
f = open("demofile3.txt",'r')
print(f.read())
f.close()

f = open("demofile3.txt",'w')
f.write("Woops! I have deleted the content!")
f.close()

print("\nAfter:")
f = open("demofile3.txt",'r')
print(f.read())
f.close()