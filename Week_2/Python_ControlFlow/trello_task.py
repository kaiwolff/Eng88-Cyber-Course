# Movie Ratings!
#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:
while True:
    rating = input("\nPlease enter the rating to receive information on it. Options are Universal, PG, 12, 15, or 18. Type 'exit' to quit: ")
    #list of acceptable inputs
    rating = rating.lower()
    valid_inputs = ["universal", "pg", "12", "15", "18"]

    if rating not in valid_inputs:
        if rating == "exit":  # this allows the user to quit if they enter 'exit'
            break
        else:
            print("Input not recognised, please try again")
            continue

    if rating == "universal":
        print("Universal - everyone can watch")
    elif rating == "pg":
        print("pg --> General viewing, but some scenes may be unsuitable for young children")
    elif rating == "12":
        print("12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
    elif rating == "15":
        print("15 --> No one younger than 15 may see a 15 film in a cinema.")
    elif rating == "18":
        print("18 --> No one younger than 18 may see an 18 film in a cinema.")

    print("\nI hope that was helpful.")

print("Thank you for using this program.")

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.