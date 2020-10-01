# Write another program that prompts for a list of numbers as above and at the end
# prints out both the maximum and minimum of the numbers and average.

sum = 0
count = 0
average = 0
min = 99999999999999
max = 0
while True:
    try:
        x = input("Enter a number: ")
        if(x == "done"):
            break
        x = int(x)
        if min > x:
            min = x
        if max < x:
            max = x
        sum = sum + x
        count = count + 1
        average = sum / count
    except:
        print("Invalid input")
print('Minimum is', min, 'Maximum is', max, 'Average is', average)

