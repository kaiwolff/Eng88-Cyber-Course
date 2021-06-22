#creatign a reptile class which inherits from the Animal class

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        #we have a keyword called super, which inherits everything from the parent class at the time of initialisation of the class.
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None #set to none because not all reptiles are this type
        self.heart_chambers = [3,4]

    def seek_heat(self):
        return "It is rainy and windy, where is the sun?"

    def hunt(self):
        return "Keep hunting for food until you get it"#

    def use_venom(self):
        return "If I've got it I'm using it."

#Now, instantiate

reptile_object = Reptile()

# #notice that A Reptile object has access to all functions from the animal, as well as it's own functions.
# print(f"This function was inherited from the animal class by the reptile class: {reptile_object.eat()}")
# print(f"This function is from the reptile class: {reptile_object.seek_heat()}")
# # This is extremely powerful, and the primary benefit of using OOP.