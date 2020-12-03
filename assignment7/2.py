def linear(tup, key):
    for nums in tup:
        if key == nums:
            return True
    return False

def binarySearch(tup, key):
    lst = list(tup)
    lst.sort()
    tup = tuple(lst)
    low , high = 0, (len(tup) - 1)
    while low <= high:
        mid = low + (high-low)//2
        if tup[mid] == key:
            return True
        elif key < tup[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


#Taking input from User and creating tuple

print("Enter All Elements : ", end=" ")
tup = tuple(map(int, input().split()))
print(tup)

#Switch Case for Python

switchCase = {1 : linear, 2 : binarySearch, 3 : "Break"}

while True:
    print("\n1.Linear Search\n2.Binary Search\n3.Break")
    print("\nEnter your Choice: ", end=" ")
    choice = int(input())
    
    if (choice == 1 or choice == 2):
        function = switchCase.get(choice)
        key = int(input("Enter the Search Value: "))
        if function(tup, key):
            print("\nFound")
        else:
            print("\nNot Found")
    elif choice == 3:
        print("Good Bye")
        exit(0)
    else:
        print("\nInvalid Choice")