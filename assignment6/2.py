elements = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = {}
for element in elements:
   if element in count:
      count[element] += 1
   else:
      count[element] = 1
for key, value in count.items():
   print(key,':',value)