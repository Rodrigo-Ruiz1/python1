print("Please fill in the blanks below:")

#example of the mad lib prompt
print("__(name)__'s favorite subject in school is ___(subject)___.")

#asking for inputs
name = input("What is your name? ")
subject = input("What is a subject? ")

#printing out the original prompt while including the user's inputs
print("%s's favorite subject in school is %s." % (name, subject))