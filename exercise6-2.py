from random import randrange

def roll(n):
    return randrange(n) + 1

n = int(input("enter you number: "))

while True:
    x = roll(n)
    print(x)
    if x >= n:
        break