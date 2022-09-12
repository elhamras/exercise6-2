user_input = int(input("enter an integer: "))
is_prime_number = True;

for x in range(1, user_input):
    input_remainder = user_input % x
    if input_remainder == 0 and (x != input_remainder and x != 1):
        is_prime_number = False

if is_prime_number:
    print(f'{user_input} is a prime number')
else:
    print(f'{user_input} is NOT a prime number')
