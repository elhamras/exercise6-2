number_list = []
number1 = input("enter your numbers: ")
while number1 != "":
     number_list.append(int(number1))
     number1 = input("enter your numbers: ")
number_list.sort(reverse=True)
print("the greatest numbers: " + str(number_list[0:5]))