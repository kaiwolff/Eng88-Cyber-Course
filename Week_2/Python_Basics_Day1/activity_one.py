#get user name, age, date of birth details.

first_name = input("Please enter your first name: ")
last_name = input("\nPlease enter your last name: ")
age = input("Please enter your age: ")

birth_year = input("\nPlease enter the year you were born:")
birth_month = input("\nPlease enter the month you were born: ")
birth_day = input("\nOn what day of that month were you born?: ")

print("Thank you. Now printing details:")
print("\nHi, {} {}".format(first_name, last_name))
print("\nYour birthdate is the {} of {}, {}. You are {} years old".format(birth_day, birth_month, birth_year, age))


#display these details, combined with a greeting message