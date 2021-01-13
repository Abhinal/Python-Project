def calculate(l,b=-99,h=-99):
    if b == -99:
        b = l
    if h == -99:
        h = l
    print('Volume: ',l*b*h)
lst = []
while True:
    choice = int(input("Enter 1 for Cube\nEnter 2 for Square Prism\nEnter 3 for Cuboid\nEnter 4 for Exit\nEnter choice: "))
    lst.clear()
    if choice == 4:
        exit('Good Bye')
    for i in range(0,choice):
        num = int(input('Enter Argument: '))
        lst.append(num)
    if choice == 1:
        calculate(lst[0])
    elif choice == 2:
        calculate(lst[0],lst[1])
    elif choice == 3:
        calculate(lst[0],lst[1],lst[2])
    else: print('Wrong Choice')