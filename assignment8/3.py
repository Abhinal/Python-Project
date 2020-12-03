dict1 = {'Name': 'Abhinav', 'Dept': 'CSE', 'Roll': '1'}
dict2 = {'College': 'STCET', 'Best Friend': 'Anamika'}
lst = [dict1, dict2]
result = {}
for dct in lst:
    for key,value in dct.items():
        result[key] = value
print(result)