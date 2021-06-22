# Python
## Python installation 3.7 or above
### Pycharm set up
#### Documentation with README.md to store on Github

- Testing the python environment `print("Hello World")`
  
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

## Running Notes - Lesson on variables

-Variables work as a placeholder to store data.
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

# Activity
#Have a 15 minute break```


#Day 2

##Topics (from Trello)
- Data Types and Operators
- Python Collections


##Operators
**Arithmetic Operators**
  `+ - / *`
##Comparison Operators
`> < == != `

##More Info:

## Arithmetic Operators

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

## Further Notes

Git Notes - available in git_notes.md

Notes on Bash Commands - see useful_bash_commands.md
