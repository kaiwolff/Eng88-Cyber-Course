# Python
 
### Why Python ?

- Very Widely used
- Huge amount of packages meaning it can be applied in a wide range of fields
- Useful for DevOps as we need to know software development
- Need to be able to understand code in order to add to it
- Easy to use, limits syntax limitations and lets you focus on solving the problem
- Emphasis on readability means it is well suited to collaborative work.

### How Python fits into DevSecOps:

- If you were to go onto a client site and be given access to a python app with the aim of securing it.

- In order to understand this code, we need to know Python.

- If we do not understand the code (not necessarily at the dev level), how could we be expected to protect it?

- Knowing at least one OOP language is vital, this can be taken across to other languages and apply security measures.

## Running Notes - Lesson on variables

- Variables work as a placeholder to store data.
- Main types are strings, Booleans, Numbers (integers and floats)
- "Quotation Marks designate strings"
- boolean holds True or False
- numbers are ints (or can be floats/doubles if decimal points involved)


Code Sample:

```# Create a variable for first name, last name and Date of Birth.

first_name = "Kai"
last_name = "Wolff"
salary = 1111 #integer

float_value = 111.112 #anything with decimal places is a float.


print("Hello, {} {}".format(first_name, last_name))
print(salary)
print(float_value)

print(type(float_value))
print(type(salary))
#can use method type() to identify what type of variable a certain variable is

#better to get user input instead.
name = input("\n Please enter your name: ")

print("Hello " + name)
```

#### Activity - Found in activity_one.py
Write code that has the following functionality:
- Create a variable for first name, last name and Date of Birth.
- Display these details, combined with a greeting message


  
### Why Python ?

- Very Widely used
- Huge amount of packages meaning it can be applied in a wide range of fields
- Useful for DevOps as we need to know software development
- Need to be able to understand code in order to add to it
- Easy to use, limits syntax limitations and lets you focus on solving the problem
- Emphasis on readability means it is well suited to collaborative work.

### How Python fits into DevSecOps:

If you were to go onto a client site and be given access to a python app with the aim of securing it.

In order to understand this code, we need to know Python.

If we do not understand the code (not necessarily at the dev level), how could we be expected to protect it?

Knowing at least one OOP language is vital, this can be taken across to other languages and apply security measures.

## Variables

- Variables work as a placeholder to store data.
- Main types are strings, Booleans, Numbers (integers and floats)
- "Quotation Marks designate strings"
- Boolean holds True or False
- Numbers are ints (or can be floats/doubles if decimal points involved)


Code Sample:

```# Create a variable for first name, last name and Date of Birth.

first_name = "Kai"
last_name = "Wolff"
salary = 1111 #integer

float_value = 111.112 #anything with decimal places is a float.


print("Hello, {} {}".format(first_name, last_name))
print(salary)
print(float_value)

print(type(float_value))
print(type(salary))
#can use method type() to identify what type of variable a certain variable is

#better to get user input instead.
name = input("\n Please enter your name: ")

print("Hello " + name)

# Activity
#Have a 15 minute break```


#Day 2

##Topics (from Trello)
- Data Types and Operators
- Python Collections
```

## Arithmetic Operators

```

##Operators
**Arithmetic Operators**
  `+ - / *`
##Comparison Operators
`> < == != `
``` 



| Operand | Description | Example |
|:---------: |:----------------------------: |:--------: |
| + | add two operands (variables) together| X + y + 2 |
| - | subtract two operands (variables) | X - y - 2 |
| * | multiply two operands (variables) | X * y|
| / | divide two operands (variables) | X / y |
| % | Modulus - remainder of the division of left operand by the right | X % y |

## Comparison Operators

| Operand | Description | Example |
|:---------: |:----------------------------: |:--------: |
| > | True if left operand is greater than the right| x > y |
| < | True if left operand is less than the right| x < y |
| == | True if both operands are equal | x == y |
| != | True if both operands are equal | x != y |
| >= | True if left operand is greater than or equal to the right| x >= y |
| <= | True if left operand is less than or equal to the right| x <= y |

# Python Collections

- Lists
- Dictionaries
- Tuples
- Sets


### What are Data Collections

- Data Collections are used to collect data
- CRUD principle: Create, read, update, delete
- Exceptions are tuples, which are immutable


## Lesson Code-Along

```#Lists
#Syntax: Use square brackets to create a list, .e.g list = []

shopping_list = ["juice", "strawberries", "yogurt", "chicken", "raspberries", "butter"]
print(shopping_list)
#print(type(shopping_list))
##same as with strings, collections are zero-indexed
#
#print(shopping_list[2]) #this prints the third value in the list.
#print(shopping_list[::-1]) #prints the list in reverse


#if we need to replace a value in the list
shopping_list[5] = "Oats"
# print(shopping_list)

#to add an item
shopping_list.append("Mangos")
print(shopping_list)

#to get rid of items

#.remove seeks out whatever is in the brackets
shopping_list.remove("Oats")
print(shopping_list)

shopping_list.pop() # pop removes the last item from the list
print(shopping_list)

```

NOTE: Lists can hold multiple data types in one list, for example integers and strings

### Tuples

```#Tuples
#Similar to lists, but immutable.
#Tuples are created with parentheses ()
# Use cases: Unchanging data. Things such as mathematical constants. Any data that once entered, shouldn't be changed.
#Also technically more memory-efficient

#in this case, using "essentials", item that will never be taken out of a shopping list

essentials = ("eggs", "milk", "coffee", "bread")
print(essentials)
print(type(essentials))

#the below will not work, since A TUPLE IS IMMUTABLE
#essentials[3] = "yogurt" 
```

### Dictionaries

```buildoutcfg
# What are dictionaries?
#contain key-value pairings
#VALUE can be string, int, list
#Syntax for creation is {}

student_1 = {
   "name" : "Kai Wolff",
    "key" : "value",
    "stream" : "Cyber Security",
    "completed_lessons" : "3",
    "completed_lessons_names" : ["Variables", "Operators", "Data Collections"]
}

print(student_1) # will print out the entirety of the dictionary as a list of key-value pairings, including any lists that are stored
print(student_1["name"]) #this will print the value associated with the key
print(student_1["completed_lessons_names"])# displays the entire list
print(student_1["completed_lessons_names"][1])# will print only "Operators", the data at the index of the value of the key.

print(student_1.keys)#this will print only the keys of the dictionary
print(student_1.values)#this will print only the values of the dictionary
```

## Sets

-Key Difference to lists is that they are not ordered.
-Can also have "frozen sets", which are very similar to tuples.
```#Code-Along - Sets
#Sets are data collections, but the key difference is that they are UNORDERED
# Syntax name = {}

car_parts = {"wheels", "doors", "engine"}

print(car_parts)

#Sets can be appended
car_parts.add("windows")
print(car_parts)

#can remove items from sets
car_parts.discard("doors")
print(car_parts)

#Frozen sets
frozen_set = ([1,3,5,26])
print(frozen_set)
#frozen sets do not change their order. they are like tupls (immutable)
```


## Functions

Blocks of code that do something you may want to call on again. Generally functions should do one thing, and do it well.

Important part of **DRY** principle ```DON'T REPEAT YOURSELF```. If you can put something into a function and re-use it, you absolutely should.

## Code-Along with annotations

```#create a basic function
#syntax is def name():

#first iteration
# def greetings():
#     return("Welcome to Cyber Security!") # return is what the function gives to something if assigned
#
# print(greetings())

#second iteration:

def greeting_user(name):
    return(f"Welcome to Cyber Security, {name}")

print(greeting_user("Kai"))

#take user name as input() and display back to user with greeting
#third iteration

def greeting_user():
    user_name = input("Hi, what is your name? ")
    return(f"Welcome to Cyber Security, {user_name}")

print(greeting_user())
```

### Taking arguments into a function

```#creatign a function that takes two arguments as integers

def add(value1, value2):
    return value1 + value2

#while this function was designed for integers, it could also take floats or strings
print(add(1.5, 1))

def subtract(value1, value2):
    return value1 - value2

print(subtract(3,2))

#activity: create multiply and divide functions

def multiply(value1, value2):
    return value1 * value2

def divide(value1, value2):
    return value1 / value2

print(multiply(2,2))
print(divide(2,2))

#exercise: give percentage

def percentage(amount, total):
    return amount*100/total
```

# Control Flow



- if, elif, else conditions
- while and for loops
- Any conditional decision-making

Control flow is very important in any programming language, as it allows us to make our programs respond to user input or special cases, and to "react" appropriately.

##Code-Along with Annotations

```#Control Flow with if, elif, else

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
```