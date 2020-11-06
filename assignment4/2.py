def reverseWord(word):
    return word[::-1]

def sliceSentence(sentence):
    words = sentence.split(" ")
    for word in words:
        print(reverseWord(word),end=" ")
    print('\n')

sentence = input('Enter a sentence : ')
sliceSentence(sentence)
