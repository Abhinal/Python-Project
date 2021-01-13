lst = []

def favSub(name,lst):
    if name == '0':
        print("Your Favourite Subjects:",end=' ')
        for i in range(0,len(lst)-1):
            print(lst[i],end=', ')
        if len(lst) > 1:
            print('and',lst[-1]+'.')
        else: print(lst[0]+'.')
        exit(0)
    else:    
        lst.append(name)

while True:
    name = input('Enter your Fav. Subject (or "0" to terminate): ')
    favSub(name,lst)