def check_permissions(age, can_drive):

    #This function checks what a user is allowed to do.
    if age < 16:
        return "You're too young, go back to school"
    elif age < 18:
        if can_drive:
            return "You can drive"
        else:
            return "You can't legally drink but your parents may give you permission with a meal"

    if age >= 18:
        if can_drive:
            return "You can vote and drive."
        else:
            return "You can vote"


while True:
    #Need to get from user: age, driving licence y/n
    age = input("Please input your age. Type 'exit' to quit the program: ")
    #option to quit
    if age.lower() == "exit":
        break
    if age.isdigit() and int(age) >= 16:
        driving_licence = input("Thank you. And do you have a driving licence? (y/n) ")
        if driving_licence.lower() == "y":
            can_drive = True
        elif driving_licence.lower() == "n":
            can_drive = False
        else:
            print("I am sorry, I didn't recognise the input. Please try again.")
            continue

    elif age.isdigit():
        can_drive = False
    else:
        print("I am sorry, I didn't recognise the input of your age. Please try again")
        continue

    #Should now have whether the user has a driving licence (impossible if under 16), and what their age is as an integer
    #Now, just call the function that checks permissions and gives message dependign on what permissions are available.

    print(check_permissions(int(age), can_drive))

print("Exiting...")



