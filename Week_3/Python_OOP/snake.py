#creating snake class, inheriting from reptile
from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.forked_tongue = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        return "I can smell the taste..."


# snake_object = Snake()
# print(f"From Animal class: {snake_object.breathe()}")
# print(f"From Reptile object: {snake_object.seek_heat()}")
# print(f"From Snake class: {snake_object.use_tongue_to_smell()}")

#as this show, iy is possible to inherit from the parent class of the parent class as well.
