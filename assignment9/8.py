friend_info = {}
while True:
    name = input("Enter your friend's name (Enter -99 to terminate or 'all' to display all data): ")
    if(name == '-99'):
        print('Good Bye')
        exit(0)
    elif(name == 'all'):
        names = []
        names = friend_info.keys()
        names = sorted(names)
        for name in names:
            print(name+':'+friend_info[name])
    elif name not in friend_info.keys():
        friend_info[name] = input("Not present\n Please Enter DOB: ")
    else: print(friend_info[name])