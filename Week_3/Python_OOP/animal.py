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

