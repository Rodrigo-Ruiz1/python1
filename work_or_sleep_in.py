user_input = int(input("Choose a number between 0-6 to see if you should sleep in: "))

if ((user_input > 0) and (user_input < 6)):
    print("Its a weekday, you should go to work.")
elif user_input == 0:
    print("Its Sunday, you should sleep in.")
elif user_input == 6:
    print("Its Saturday, you should sleep in.")
else:
    print("Sorry, that number is invalid")