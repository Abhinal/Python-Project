def printIntials(fullname):
    words = fullname.split()
    for i in range(len(words)-1):
        temp = words[i]
        words[i] = temp[0].upper()+'.'
    words[-1] = words[-1].capitalize()
    return ''.join(words)

fullname = input("Enter fullname : ")
print(printIntials(fullname))