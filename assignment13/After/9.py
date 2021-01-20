def compare(f1, f2):
    if f1.read() == f2.read():
        print("Same")
    else:
        print("Different")

f1 = open("demofile.txt","r")
f2 = open("demofile9.txt","r")

print("Before:")
compare(f1, f2)

f2 = open("demofile9.txt","w")
f2.write("Hey I am new here.")
f2 = open("demofile9.txt","r")

print("\nAfter:")
compare(f1, f2)
