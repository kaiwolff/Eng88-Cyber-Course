class Rating_Explainer:

    def __init__(self):
        self.avail_ratings = {
            "U" : "Everyone can watch",
            "PG": "General viewing, but some scenes may be unsuitable for young children",
            "12": "Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.",
            "15" : "No one younger than 15 may see a 15 film in a cinema",
            "18" : " No one younger than 18 may see an 18 film in a cinema."
        }

    def explain_rating(self):
        #added option to return "exit" in case this method/object was to be used in a separate while loop
        while True:
            rating = input(f"Which rating are interested in? Options are {self.avail_ratings.keys()}. Type 'exit' to exit: ")
            #check for exit
            if "exit" in rating.lower():
                return "exit"
            elif rating in self.avail_ratings.keys():
                print(self.avail_ratings.get(rating))
            else:
                print("Input not recognised, please try again.")
                continue


explainer = Rating_Explainer()
explainer.explain_rating()