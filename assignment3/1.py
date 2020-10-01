# Write a program to sum up to n numbers.

try:
    num = int(input("Enter the value of n: "))
except:
  print("Invalid input")
  exit(0)
sum = 0
for i in range(0,num,1):
    sum = sum + num
    num = num - 1
print('sum is', sum)



