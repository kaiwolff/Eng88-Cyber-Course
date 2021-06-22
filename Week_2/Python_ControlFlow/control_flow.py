#Control Flow with if, elif, else

#First let's set up something we check for.

# weather = "rainy"
#
# #if the boolean given to an if statement is true, the indented block runs
# if weather == "sunny": #remember to use the colon. Also to indent
#     print("Enjoy the weather!")
#
# elif weather == "rainy":#this will run shoudl the if statement not be true, but another set of conditions is fulfilled
#     print("Remember to take an umbrella")
#     #can have as many statements as we want. Cna also nest if statements, or have several conditions for one statement
# else: #this code will run if none of the other options are fulfilled
#     #Good practice is to have a contingency should the if statement not activate, so that we can be sure that the code actually ran.
#     print("'Something went wrong, input was not recognised")
#     #note: a while loop is a better option if we are prompting the user/client/customer for data in a particular format.
#     #havign several if statements in sequence will executed
#     #Havign several "if" blocks will check each conditions, elif will only be checked
#
# #as an example, age restrictions on cinema tickets. See cinema_checker.py


#Loops
#used to iterate through data collections, e.g. Lists, Dicts, Sets, etc.
#Can also iterate through strings
#First playaround with a for loop
# list_data = [1, 2, 3, 4, 5]
# for list in list_data: #this will iterate through list_data, giving each index the name "list" in the code block
#     if list == 5:
#         print("found 5")
#     if list == 2:
#         print("found 2")
#     if list == 3:
#         print("found 3")
#     print(list)
# else:
#     print("Better luck next time")
#playing with a dictionary
# student_1 = {
#    "name" : "Kai Wolff",
#     "key" : "value",
#     "stream" : "Cyber Security",
#     "completed_lessons" : "3",
#     "completed_lessons_names" : ["Variables", "Operators", "Data Collections"]
# }
# for data in student_1.values(): #.values means it will assign the VALUE to data. Default with a dict is to assign the key
#     if data == "Cyber Security":
#         print("Great Course Choice!")
#         break
#     print(data)
# #notice the nesting of loops. This is what makes programs powerful.

#While loops - these stay active WHILE some condition is active

user_prompt = True
while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer as a digit.")

print(f"Your age is {age}")