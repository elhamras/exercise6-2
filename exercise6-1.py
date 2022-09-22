from random import randrange

def roll():
    return randrange(6) + 1


while True:
    x = roll()
    print(x)
    if x == 6:
        break

