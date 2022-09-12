import random
dicelist = [ ]
x = 1
count = int(input("enter the dice rolling count: "))
for x in range(count):
    dice = random.randint(1,6)
    dicelist.append(dice)
print(dicelist)
sumrolling = sum(dicelist)
print(sumrolling)
