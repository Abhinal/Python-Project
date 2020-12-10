words = ['Abhinav','Agarwal','Golu',('Ghanshyam','Saraf'),'Abhi']
count = 0
for word in words:
    if isinstance(word, tuple):
        break
    count += 1
print(count)