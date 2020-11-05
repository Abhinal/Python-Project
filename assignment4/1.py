def checkPalindrome(string):
    reverse = string[::-1]
    if(reverse==string): print('String is Palindrome')
    else: print('String is not Palindrome')

string = input('Enter a string : ')
checkPalindrome(string)
