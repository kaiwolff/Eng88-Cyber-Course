# age_permissions Readme

This program prompts the user to let us know their age. In order to be continuous, I put the main body in a while loop that will be broken if the user types "exit" when prompted.

Initially, I focused on getting user input:

```
while True:
    #Need to get from user: age, driving licence y/n
    age = input("Please input your age. Type 'exit' to quit the program: ")
    #option to quit
    
```
With this input, we first check whether the user wants to quit. the ```.lower``` allows exiting with some minor typos, such as typing "EXIT" or "Exit":
```
    if age.lower() == "exit":
        break
        
```
Next, we check whether the age was in an acceptable format using ```.isdigit()```, and prompt the user to tell us if they can drive should they be over 16. The variable ```can_drive``` will be set to False if the user is under 16, since it shouldn't be possible to have a driving licence at that age. If the user didn't enter y or n as a response, the loop resets and the user will be asked for their data again.
```
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
        
```

Having obtained the necessary info and made sure it is in the correct form, we can now pass these variables to the control flow. I packaged this in a function for neatness, so the last line in the while loop is just a call to the function inside a print statement. As age is still a string at this stage, we conver tit to an integer for use in the function:

```
    print(check_permissions(int(age), can_drive))

```
Should the while loop be exited, the user gets a message to let them know the program is ending:

```
print("Exiting...")
```


#### The check_permissions function

With the variables ```age``` and ```can_drive```, we run through a series of checks, and return the appropriate response:


```def check_permissions(age, can_drive):

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
 ```
A second iteration might clean up the structure of these if statements, as they could be presented more neatly.