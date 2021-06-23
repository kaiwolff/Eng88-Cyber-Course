# Python Week 2 - Combined Notes

## Introduction to Object-Oriented Programming

### Packages

Packages and modules are pre-made blocks of code that can be used to perform a particular task without the need to add your own code. They can be simply imported using the ```import``` command. It is also possible to import individual functions using the command ```from [package] import [function]```. This has the advantage that the function can suimply be called by its name, rather than needing to specify the package name for every function call.

#### os and sys

These two packages are useful for doing system-related tasks, such as getting the current working directory (an obvious use case for this would be constructing a filepath for saving or retrieving files).

##### Math - Sample code discussion

The ```math``` library contains a large amount of functions and values commonly used in mathematics. These are commonly used to perform operations such as rounding.

An example of this is shown here:

```python

from random import random
import math

num1 = random()
print(num1)
if num1 >= 0.5:
    print(math.ceil(num1))
else:
    print(math.floor(num1))
```

We are actually using two packages here: math and random. Howver, we only imported the function ```random``` from the package of the same name, which means we can call it like a function and don't have to mention the name of the packaged anymore.

To use the ceil and floor functions, we use the syntax ```math.[function]```.

#### Lambda
This type of function takes multiple arguments and returns a singular value. It has built-in functionality that helps us work out certain things

### The Four Pillars of OOP

- Abstraction
- Inheritance
- Encapsulation
- Polymorphism

#### Abstraction

Abstraction is the process of taking away characteristics to reduce something to an essential set of characteristics. When modelling objects using classes ,minimising the amount of information necessary for a user of a function to know in order to get usable software.

#### Inheritance

This means that we can, and should, create "child classes", which take the properties of a "parent class" and "inherit" their traits as a starting point. For example, you might have a person class, but then have classes based on this such as worker, student, or similar.

#### Encapsulation

This means hiding data internal to a class from a client or external user. Use underscores to signal to other programmers that we do not want a variable changed. e.g. to indicate that ```var``` is private, we would define it as ```_var``` in our function.

#### Polymorphism

This is the philosophy of having many forms available. This means you can overwrite methods from a parent class without changing the parent class. This means that if you had an employee class, you might write a different "pay" method depending on the way the employee was paid (e.g some are salaried, some hourly, some get bonuses, etc etc.)


#### In practice - Animal class and child classes

To demonstrate this, we create a quick class called Animal, containing a few typical features an animal might have:

```python

#animal fil to create Animal class
#Notice the convention. Classes are in CamelCase

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "nom nom nom."

    def move(self):
        return "moving all around the world"


#now, we need to create an object of our Animal class to test.

# cat = Animal()
# print(cat.breathe()) # breathing for cat is abstracted. It is possible to just call the breathe function.

#Important point is that a class needs to be instantiated (an object of the class needs toi be created) in order to call the methods


```

we can import this into another class, which we note as a child of the Animal class using the syntax ```ChildClass(ParentClass```. If we are writing in a separate file as we have done here, we also need to import the parent class we are basing our work on using, in this case, the command ```from animal import Animal```. We can also inherit further, with "grandchild" classes, which we have done in the other files. Notice that we can call all the way up the inheritance tree, even being able to call Animal methods in the snake class even though it is the "great-grandchild" of that class.

Taking the example below, we see the great-grandchild of Animal, Python. An object of the python class can use methods from any of the predecessors, as the print statements show:

```python
from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "yum yum yum, that was a big meal"

    def climb(self):
        return "Up we go"

    def shed_skin(self):
        return "Time to grow out of myself"


my_python = Python()

print(f"From Animal class: {my_python.breathe()}")
print(f"From Reptile object: {my_python.seek_heat()}")
print(f"From Snake class: {my_python.use_tongue_to_smell()}")
print(f"From Python class: {my_python.digest_large_prey()}")
```


## Simple Test Case - A Calculator in Two Parts

This task is similar to the one done in Week 1, but to demonstrate the ability to inherit, it is split into two parts, a simple calculator (stored in oop_calculator), and a slightly mroe advanced calculator stored in functional_calculator.

We start with the SimpleCalculator class:

```python
class SimpleCalculator:

    def add(self, value1, value2):
        return value1 + value2


    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2
```

This contains four functions, for addition, subtraction, multiplication and division. If an objec tof SimpleCalculator is instantiated, the functions can be accessed, for example like below:

```python
calculator_object = SimpleCalculator()
print(calculator_object.add(1,2))
```

We now want to add mroe functionality to the calculator, in this case a check whether two numbers are divisible, a converter for inches to centimetres, and a function to calculate the area of a triangle.

To do this, we create a child class of SimpleCalculator, which I have called FunctionalCalculator:

```python

class FunctionalCalculator(SimpleCalculator):
    #add mroe functionality compared to the simple calculator
    def __init__(self):
        super().__init__()

    def inchtocm(self, value1):
        return value1 * 2.54

    def triangle_area(self, height, width):
        return height*width/2

    def divisible(self, value1, value2):
        if value2 == 0:
            return False
        elif value1 % value2 == 0:
            return True
        else:
            return False

```

The functions we have added are available only in FunctionalCalculator. However, the key thing is the below block of code:

```python
    def __init__(self):
        super().__init__()
```

using the ```super().__init__()``` statement means we are telling the interpreter to set up the initial coinditions of our class in the same way as its parent class, or superclass. We can therefore access all of SimpleCalculator's functions, with the new functions being added on for our FunctionalCalculator class. This is what is known as inheritance, and a key aspect of OOP.

The examples of python code for this section can be found in /Week3/Python_OOP if needed.

## Files and Error Handling

### Errors and Exception handling

`try` `except` and `finally` blocks are the core of error handling.

`try` is the first attempt. This is what the code will attempt first

`except` will run if the try attempt throws an error. This can be set to 

`finally` works as an else statement would - should the except block not trigger


In Practice, one of these looks like this:

```python
try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
    #creating aliases. The as portion defines the error message as a variable
    print("order.txt not found\n" + str(errmsg))
finally:
    print("Thank you for visiting, hope to see you again!")
    #This will run, regardless of whether the other blocks run.
```

The try portion will only work if there is a file with the given name in the directory, otherwise the except block will kick in. The ```finally``` will trigger at the end.

### Handling files - Reading files



- We have already opened a file and we have begun to handle some of the errors that can come from it but there are many more options to be applied to the opening of a file. The key part is adding a mode to the file opening



`open(file, mode)`



| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'r+' |This will open a file for reading and writing (updating)|

### Practice - A simple order file builder

In practice, this is used in the following two functions, which read and write to a file:
```python
def open_using_with_and_print(file):

    try:
        with open("order.txt", "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        print(f"{file} not found\n" + str(errmsg))

    finally:
        print("Thank you for visiting, hope to see you again!")
        #This will run, regardless of whether the other blocks run.


#Mini-Task: Create a function called open_with_to_write_to_file to write/add/append
#display the data with the added items - item names - Pizza, Cake, Avocado, Biryani, Pasta

def open_with_to_write_to_file(file, item_list):
    try:
        with open("order.txt", "a") as file:
            for item in item_list:
                file.write(f"\n{item}")

    except FileNotFoundError as errmsg:
        print(f"{file} not found\n" + str(errmsg))

    finally:
        print("Thank you for adding to the order, hope to see you again!")
        #This will run, regardless of whether the other blocks run.
```

I have set this up to take a list of items to add, and a filename. The list and function call is below:

```python
order_list = ["Pizza", "Cake", "Avocado", "Biryani", "Pasta"]

open_with_to_write_to_file("order.txt", order_list)
```

#### Re-Working

To avoid repeatedly typing the same link, I updated the function to read the file into a variable, then checking if the designated input from our list is inside the file. The appending only occurs if the requested addition is not in ```file_contents```


```python

def open_with_to_write_to_file(file, item_list):
    try:
        with open("order.txt", "r+") as file:
            file_content = file.read()
            for item in item_list:

                if item in file_content:
                    print(f"{item} is already in order")
                else:
                    file.write(f"\n{item}")
                    print(item)
```

the except and finally blocks remain unchanged.
## Test-Driven Development

The concept behind this is to write the tests for a program to be considered functional first, and then write the code to pass these tests. Once the
## TDD Exercise

Trying out a TDD approach to writing a calculator

First, we ensure that pytest is installed as we need this to run our tests.

Since we are trialling Test-Driven Development, we write the tests before the code, defining what functions we want to have in our calculator and what we want them to return for our test cases.

To do this, we create a class that inherits from the TestCase class in the unittest library. This class lets us run methods to test the functionality of our code. We also need to have imported the classes we want to test.

After that we simply define what we require the test case to return when we run a function with a set of inputs. Instantiating an object of the testable code in our test case and then defining the functions lets us run the test case to make sure the code does what we want it to. The full code is below:

```python
#this file requires pytest to be installed.
import pytest
import unittest

from functional_calc import FunctionalCalculator

class FunctionalCalcTest(unittest.TestCase):

class FunctionalCalcTest(unittest.TestCase):

    calc = FunctionalCalculator()

    def test_add(self): # naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter recognises it as a testcase.
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 4), 0.5)

    def test_inch_to_cm(self):
        self.assertEqual(self.calc.inch_to_cm(2), 5.08)

    def test_triangle_area(self):
        self.assertEqual(self.calc.triangle_area(2,2),2.0)

    def test_divisible(self):
        self.assertEqual(self.calc.divisible(2,0), False)
        self.assertEqual(self.calc.divisible(2,3), False)
        self.assertEqual(self.calc.divisible(2,2), True)
        
    
    def test_percentage(self):
        self.assertEqual(self.calc.percentage(1,2), 50.0)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(self,1,2), 1)


```

Notice that all testing functions start with `test`, which is important as it is needed for the interpreter to recognise them as tests. Also notice that the test of divisible has three test cases, one for each branch of the intended control flow.

Now that we have defined what tests we want our code to pass, we write code to pass these tests. As this exercise is about the TDD approach, I took my calculator code from a previous iteration. I did this through two classes:

```python
#file named oop_calculator
class SimpleCalculator:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

```
We have to have the parent class, SimpleCalculator available.

```python

class FunctionalCalculator(SimpleCalculator):
    #add mroe functionality compared to the simple calculator
    def __init__(self):
        super().__init__()


    def inch_to_cm(self, value1):
        return value1 * 2.54

    def triangle_area(self, height, width):
        return height*width/2

    def divisible(self, value1, value2):
        if value2 == 0:
            return False
        elif value1 % value2 == 0:
            return True
        else:
            return False
```
This code fails two of the tests, as the functions modulus and percentage are not yet available. Therefore, we have to write code to pass our tests, meaning we need to add the below to `FunctionalCalculator`:
```python

    def percentage(self, value1, value2):
        if value1 >= 0:
            return value1*100/value2

    def modulus(self, value1, value2):
        return value1 % value2

```

Simple Calculator could also be tested separately, meaning that we would only need to test the additional functions in functional_calc.

#### Notes:

- Test cases have to start the function name with `test` in order to be recognised by the interpreter. 
- Ideally, tests should cover any ways a user might conceivably input something that causes problems with the code.

## APIs

Stands for Application Programming Interface.

**An API (Application Programming Interface) is a set of functions that allows applications to access data and interact with external software components, operating systems, or microservices. To simplify, an API delivers a user response to a system and sends the system's response back to a user.**

Need to have:


 - network connectivity
 - App used must be accessible at both ends

There are status codes, which are sometimes seen in for example websites (e.g. the infamous 404 error).

API Calls are behind almost any tracking in apps, e.g. live delivery tracking. Almost any automated messages require API calls. Generally speaking, APIs allow us to communicate with websites and applications. An exercise in using API calls was described in the api_task_readme, providing a more hands-on demonstration of API functionality.

Following on from this, I added a function that shows the user the available keys and lets them choose a piece of data they would like to have displayed.

```python

import requests
#need ot import json to read "bytes" class
import json
def get_postcode():
    #prompts user for input of a postcode. runs until valid postcode in correct format is entered
    while True:
        postcode = input("please enter a valid UK postcode, without any spaces:")

        if postcode_exists(postcode) == True:
            return postcode
        else:
            print("Invalid postcode")
            continue

def postcode_exists(postcode):
    #checks if postcode returns status 200 from postcodes.io
    postcode = postcode.lower()
    post_api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")

    if str(post_api_response.status_code) == "200": #200 is the response that signifies the website is responding.
        #print(f"Postcode {postcode} exists. Status code {post_api_response.status_code}")
        return True
    else:
        #print("The postcode is incorrect, please enter the correct postcode.")
        return False

def get_constituency(postcode):
    #should print the parliamentary constituency.
    api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")
    constituency = json.loads(api_response.content)["result"]["parliamentary_constituency"]
    print(f"Your constituency is: {constituency}")

def collect_info(postcode):
    #quick function to collect available info into a dictionary:
    api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")
    #json loads converts the json into a python dictionary that I can actually work with
    return json.loads(api_response.content)["result"]

def show_info(postcode):
    available_info = collect_info(postcode)
    print("here is the available information")
    for key in available_info.keys():
        print(key)

    desired_info = input("which bit of info would you like to know? ")
    if desired_info in available_info.keys():
        print(available_info[desired_info])

postcode = get_postcode()
# get_constituency(postcode)
# show_info(postcode)
```