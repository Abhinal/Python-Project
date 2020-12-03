dict1 = {'a':1, 'c':3, 'b': 2}
dict2 = {}
lst = [dict1, dict2]
for dct in lst:
    if (len(dct) == 0):
        print("Oops!",dct,"is empty.")
    else: print("Wooah!",dct,"is not empty")