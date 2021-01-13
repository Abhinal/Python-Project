from random import randint

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

for i in range(6000):
    dice = randint(1, 6)
    if dice == 1:
        count1 += 1
    elif dice == 2:
        count2 += 1
    elif dice == 3:
        count3 += 1
    elif dice == 4:
        count4 += 1
    elif dice == 5:
        count5 += 1
    else:
        count6 += 1

print("You rolled\n")
print(f"One: {count1} times.")
print(f"Two: {count2} times.")
print(f"Three: {count3} times.")
print(f"Four: {count4} times.")
print(f"Five: {count5} times.")
print(f"Sixe: {count6} times.")