# Lesson Code-Along
#Lists
#Syntax: Use square brackets to create a list, .e.g list = []

#list are MUTABLE

# shopping_list = ["juice", "strawberries", "yogurt", "chicken", "raspberries", "butter"]
# print(shopping_list)
# print(type(shopping_list))
#
# #same as with strings, collections are zero-indexed
# #
#
# print(shopping_list[2]) #this prints the third value in the list.
# print(shopping_list[::-1]) #prints the list in reverse
#
#
#
##if we need to replace a value in the list
# shopping_list[5] = "Oats"
# print(shopping_list)
#
# #to add an item
# shopping_list.append("Mangos")
# print(shopping_list)
#
# #to get rid of items
#
# #.remove seeks out whatever is in the brackets
# shopping_list.remove("Oats")
# print(shopping_list)
#
# shopping_list.pop() # pop removes the last item from the list
# print(shopping_list)

#Tuples
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