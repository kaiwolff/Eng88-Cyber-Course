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