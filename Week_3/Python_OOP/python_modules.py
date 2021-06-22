#What are Python Modules/packages?

#Packages and nmodules are built-in blocks of code you can use to fulfil certain purposes, such as generating a random number, or performing a particular mathematical operations. These are available from Python's libraries directory, and can be imported using the "import" command. There is also full documentation available, if the user comes across a function in someone else's code and isn't sure what the function actually does.
#Let's try this out
#
# import random
# print(random.random())
#the above calls the "random" fucntion frokm teh random library to generate a number between 0 and 1. Can also import only singular functions using, for exampel "from random import random. This will only import the particular function. The advantage is that we would no longer have to type random.random(), but rather can just type random() for a random number.

# from random import random
# print(random())
# import math
#
# num1 = 23.66
# print(num1)
# print(math.ceil(num1))
# print(math.floor(num1))

#task:generate a number USING RANDOM. if the number inumber input is >= .50, apply ceil. if less than .50, apply floor()/

# from random import random
# import math

# num1 = random()
# print(num1)
# if num1 >= 0.5:
#     print(math.ceil(num1))
# else:
#     print(math.floor(num1))
#
#
# random_number = random()
# print("This is a randomly generated: " + str(random_number))
# if random_number >= 0.5:
#     print(f"This value was rounded up with math.ceil: {math.ceil(random_number)}")
# else:
#     print(math.floor(random_number))
#     print(f"This value was rounded down with math.floor: {math.floor(random_number)}")

#Taking a look at os
#os , sys is used to the get information about localhost/your machine such as name, path, etc.

import os, sys, datetime
#
# print(os.cpu_count())
# print(datetime.datetime.today())
#
# # % provides remainder value
# print(math.remainder(1, 5))



#
# working_directory = os.getcwd()
# print(f"You are in {working_directory}")
#
# system_path = sys.path
# print(f"This is the path{system_path}")
#
# def current_system_path():
#     print(f"This is your current path:")
#     return sys.path
#
# print(current_system_path())
#
# def current_directory():
#     print("This is you working directory")
#     return os.getcwd()
#
# print(current_directory())
#
# print(math.pi)

#lambda functions
#These tyake in several values, and return a singular value.
#They are defined using the syntax arguments : expression
#For example:

addition = lambda num1, num2 : num1 + num2

print(addition(1,2))
#The above would return the two input arguments added together inside the print statement. This is similar to the add function previously defined in our calculator, for example.
#These are commonly used in banking, for example, as there are built-in functionalities that allow some calculations