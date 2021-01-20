f = open("demofile.txt",'r')
print("1st line:" , f.readline())
print("2nd line:" , f.readline())

f.seek(0)
print("1st 5 letters:" , f.read(5))

f.seek(0)
print("Content of file:")
for content in f:
    print(content,end="")
print()
f.close()