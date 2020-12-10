stack = []

while True:
    print("\n1.For add data\n2.For pop\n3.Exit")
    print("\nEnter your Choice: ", end=" ")
    choice = int(input())
    
    if(choice == 1):
        key = int(input("Enter data: "))
        stack.append(key)
        print(stack)
    elif(choice == 2):
        stack.pop()
        print(stack)
    elif(choice == 3):
        print("Good Bye")
        exit(0)
    else:
        print("\nInvalid Choice")