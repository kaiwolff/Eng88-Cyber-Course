import time
import datetime

while True:

    birthday = input("\nPlease enter your DOB in the format DD/MM/YYYY. Enter 'exit' to quit the program: ")

    if birthday == "exit":  # this allows the user to quit if they enter 'exit'
        break
    else: #this will attempt to convert the DOB into a datetime, and will re-prompt if the input isn't recognised
        try:
            birthday_time = time.strptime(birthday, "%d/%m/%Y")
            #now have a time_struct object. convert to datetime
        except:
            print("Input not recognised, please try again")
            continue

    now = datetime.date.today()
    birthdate = datetime.date(birthday_time[0], birthday_time[1], birthday_time[2])

    age = ((now-birthdate).days)/365.25
    print(f"Your age is {int(age)}")

    if int(age) >= 18:
        print("You can watch any films we have")
    elif int(age) >=15:
        print("You may watch ratings 15, 12, PG, or U")
    elif int(age) >= 12:
        print("You may watch ratings 12, PG, or U")
    elif int(age) < 12:
        print("You may watch U-rated films, or PG films if you are with a parent")

    rating = input("\nPlease enter the age rating of the film you are trying to watch (U, PG, 12, 15, or 18): ")

    can_watch = False  # default case is to not allow sale, just in case
    if rating.isdigit() or rating == "U" or rating == "PG":

        if rating == "U":
            can_watch = True
        if rating == "PG" and int(age) >= 12:
            can_watch = True
        elif rating == "12" and int(age) >= 12:
            can_watch = True
        elif int(age) >= 18:
            can_watch = True
    else:
        print("The input for rating was not recognised. Please try again")
        continue

    #finally, display outcome
    if can_watch:
        print("You can buy this ticket")
        break
    else:
        print("You may, unfortunately, not watch this movie.")
        break

print("Thank you for using cinema_checker")