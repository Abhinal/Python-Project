def changeSentence(sentence, word):
    reverseWord = word[::-1]
    sentence = sentence.replace(word,reverseWord)
    return sentence

sentence = input('Enter a sentence : ')
word = input('Enter a word : ')
print(changeSentence(sentence, word))
