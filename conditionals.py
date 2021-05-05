import random

#because the input we ask for in line 4 is a number, we must make it an integer (using int) so we can compare it properly in line 9 (using the ==)
user_input = int(input("Guess a number: "))
print(user_input)

magic_number = random.randint(0,10)

if user_input == magic_number:
    print("YOU GOT IT!!")
else:
    print("BZZZZZZZZT WRONG!!! It was %d" % (magic_number))