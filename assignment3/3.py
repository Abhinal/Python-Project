#Write a program to find Armstrong for a range 1 to 1000.

print('Armstrong Number in a range 1 to 1000 are :')
for num in range(1, 1000):
    count = 0
    temp = num
    while temp > 0:
        temp = temp // 10
        count = count + 1
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit**count
        temp = temp // 10
    if num == sum:
        print(num)