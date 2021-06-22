#Arithmetic Operators
# + - / *
#Comparison Operators
#>
# <
# ==

# value1 = 6
# value2 = 7
#
# # print(value2 > value1) #returns true if value2 is bigger than value1
# # print(value1 > value2) #as above but values reversed
# # print(value1 + value2)
# # print(value1 - value2)
# # print(value1 >= value2)
# # print(value1 != value2)
#
#
# #Built in methods available that give us boolean outcome
# #e.g.
#
# name = "James"
# #isalpha checks if all the character are letters
# print(name.isalpha())
#
# #if this was a number, would need to use casting:
#
# # age = str(2)
# # print(age.isalpha())
# print(name[0])
# print(name.startswith(name[0].upper()))

#Strings Concatenation and Casting - started at 15:30 - 18/05/2021
#
# greetings = 'Hello World!'
# #can have single or double quotes, this makes no difference to the python interpreter
# print(greetings)
# #For an individual letter, remember that this is zero indexed. This means it goes from 0 to n-1
# #where n is the number of letters.
#
# #String Slicing (taking out part of a string)
# #requires proper uise of index. syntax [:x] - everything up to x. [x:] - everythign after x [
# print(greetings[-6:])
#can also strip whtiespace from end of strings.
#
# white_spaces = "Lots of spaces here.                                                     "
# print(len(white_spaces))
# print(len(white_spaces.strip()))
#
# example_text = "here's SOME text, with a lot of text inside."
# print(example_text.count("text")) #counts how many times the argument stringis in the target string
#
# #other ways of messign around with text.
# print(example_text.lower()) # makes everythign lower case
# print(example_text.upper()) # makes everything upper case
# print(example_text.capitalize()) # capitalises the first letter of the string.
#
# print(example_text.replace("with", "containing"))

#Concatenation: Combining values, variables, strings

first_name = "James"
last_name = "Bond"
age = "45"

# print(first_name + " " + last_name + ", " + age)

#exercise: converst age string into integer, print out age as integer and type
print("{}, {}".format(int(age), type(int(age))))

#can also do
int_age = int(age)
print("{}, {}".format(int_age, type(int_age)))
#also
print(f"{int(age)}, {type(int(age))}")

#next exercise:

