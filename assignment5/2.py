first = int(input("Enter first number: "))
last = int(input("Enter last number: "))


a = 2
b = 3
temp = 0
while(a<last):
    diff = b - a - 1
    if diff>0 and b>=first:
        for i in range(1,diff + 1):
            x = a + i
            if x <= last and x < b:
                print(x,end=" ")
    temp = a+ b
    a = b
    b = temp
