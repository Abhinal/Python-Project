words = ["Abhinav","Anamika","Bittu","Bobby","Chandra","Charvi","Devanshu","Dhiraj","Eklavya","Frogy","Gautam","Guddu","Hero","Hitesh"]
key = input("Enter any alphabet: ")
result = []
for word in words:
    if(word[0]==key.upper()):
        result.append(word)
if(len(result) != 0):
    print(result)
else: print("Nothing to show")