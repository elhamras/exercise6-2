value = int(input("enter the hemogolobin value: "))
if 117 <= value <= 155:
    gender = (input("female"))
    print("normal")
    if 134 <= value <= 167:
        gender = int(input("male"))
        print("normal")
else:
    print("unormal")
