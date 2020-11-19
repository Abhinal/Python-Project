string = input("Enter the string: ")
word = 1
vowel = 0
consonant = 0
punctuations = 0
for letter in string:
    if(letter.isalpha()):
        if(letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='U' or letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U'): vowel += 1
        else: consonant += 1
    elif(letter=='.' or letter==',' or letter=='?' or letter=='!' or letter==':' or letter==';' or letter=='-' or letter=='_' or letter=='(' or letter==')' or letter=='{' or letter=='}' or letter=='[' or letter==']' or letter=="'" or letter=='"' or letter=='/'): punctuations += 1
    elif(letter==' '): word +=1
print('vowels =',vowel)
print('consonant =',consonant)
print('word =',word)
print('punctuations =',punctuations)