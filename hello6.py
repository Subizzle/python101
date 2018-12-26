first_name = input("What is your first name? ")
print("Hello," , first_name)
if first_name == "Chris":
    print(first_name, "is learning Python.")
elif first_name == "Maximiliane'":
    print(first_name, "is learning with fellow students in the Community! Me too!")    
else:
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {}! If you're confident with your reading already...".format(age))
    print("You should totally learn Python, {}!".format(first_name))    
print("Have a great day {}!".format(first_name))
