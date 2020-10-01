# Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers. If
# the user enters anything other than a number, detect their mistake using try and
# except and print an error message and skip to the next number.


sum=0
count=0
average=0
while True:
    try:
        x=input("Enter a number:")
        if(x=="done"):
            break
        x = int (x)
        sum = sum + x
        count = count + 1
        average = sum / count
    except:
        print("Invalid input")
print('sum is',sum,'count is',count,'average is',average)
