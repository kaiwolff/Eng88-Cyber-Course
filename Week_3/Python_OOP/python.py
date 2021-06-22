#python class, which will inherit from Snake class

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "yum yum yum, that was a big meal"

    def climb(self):
        return "Up we go"

    def shed_skin(self):
        return "Time to grow out of myself"


my_python = Python()

print(f"From Animal class: {my_python.breathe()}")
print(f"From Reptile object: {my_python.seek_heat()}")
print(f"From Snake class: {my_python.use_tongue_to_smell()}")
print(f"From Python class: {my_python.digest_large_prey()}")