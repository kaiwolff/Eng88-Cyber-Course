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
#for the above: "Name of the dictionary with key in square brackets fetches the list. The square brackets with the index number then fetches the content of that index
print(student_1.keys)#this will print only the keys of the dictionary
print(student_1.values)#this will print only the values of the dictionary