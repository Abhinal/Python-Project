print("Before:")
f = open("demofile2.txt",'r')
print(f.read())
f.close()

f = open("demofile2.txt", "a")
f.write("\nNow we have one more line.")
f.close()

print("\nAfter:")
f = open("demofile2.txt",'r')
print(f.read())
f.close()
