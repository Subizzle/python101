name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops

validation = input("{}, do you understand Python while loops?\n(Enter yes/no.)".format(name))
    
# TODO: Write a while statement that checks if the user doesn't understand while loops
while validation.lower() != "yes":

    # TODO: Since the user doesn't understand while loops, let's explain them.
    print("Ok, {}, while loops in Python repeat as long as a certain Boolean condition is met.\n{} do you now understand Python while loops?".format(name, name))
    
    # TODO: Ask the user again, by name, if they understand while loops.
    validation = input("Enter Yes/No please. ")

# TODO: Outside the while loop, congratulate the user for understanding while loops    
print("That's great, {}. I'm pleased that you understand loops now. That was getting repetitive.".format(name))
