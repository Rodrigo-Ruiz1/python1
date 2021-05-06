#int will turn the user_input string into an integer, allowing us to compare it in our if/else statements
user_input = int(input("Choose a number between 0-6 to see what day of the week it corresponds with: "))

if user_input == 0:
    print("%d corresponds with Sunday" % (user_input))
elif user_input == 1:
    print("%d corresponds with Monday" % (user_input))
elif user_input == 2:
    print("%d corresponds with Tuesday" % (user_input))
elif user_input == 3:
    print("%d corresponds with Wednesday" % (user_input))
elif user_input == 4:
    print("%d corresponds with Thursday" % (user_input))
elif user_input == 5:
    print("%d corresponds with Friday" % (user_input))
elif user_input == 6:
    print("%d corresponds with Saturday" % (user_input))
else:
    print("That is an invalid input")

