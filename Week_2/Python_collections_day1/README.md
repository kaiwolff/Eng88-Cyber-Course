# Python Collections

- Lists
- Dictionaries
- Tuples
- Sets


### What are Data Collections

- Data Collections are used to collect data, oddly enough
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