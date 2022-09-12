city_name = []
print("Enter 5 city name: ")
for x in range(0,5):
    name = input()
    city_name.append(name)
count = 0
x = 1
for count in city_name:
    print(f' city {x} is: {count}')
    x = x+1


