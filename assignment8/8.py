old_dict = {'a':1, 'b':2, 'c': 3}
new_dict = {}
for key,value in old_dict.items():
        new_dict[value] = key
print("old_dict",old_dict)
print("new_dict",new_dict)