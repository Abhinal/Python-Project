a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if(a >= b):
    if(a >= c):
        print('Max number:',a)
        if(b >= c):
            print('Min number:',c)
        else:
            print('Min number:',b)
    else:
        print('Max number:',c,'\nMin number:',b)
elif(b >= c):
    print('Max number:',b)
    if(a >= c):
        print('Min number:',c)
    else:
        print('Min number:',a)
else:
    print('Max number:',c,'\nMin number:',a)