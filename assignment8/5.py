dct = {'a':1, 'c':3, 'b': 2}
new_dict = sorted(dct)
result = {}
for key in new_dict:
    result[key] = dct[key]
print("unsoted:",dct)
print("sorted:",result)