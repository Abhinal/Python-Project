def takeInput():
    number = input("Enter number: ")
    return number

lst = []

is_loop_on = True

while is_loop_on:
    number = takeInput()
    if number.lower() == 'done':
        is_loop_on = False
    else:
        try:
            lst.append(int(number))
        except:
            print('Please input valid number.')

print(f"Total: {sum(lst)}")
print(f"Count: {len(lst)}")
print(f"Average: {sum(lst)/len(lst)}")
