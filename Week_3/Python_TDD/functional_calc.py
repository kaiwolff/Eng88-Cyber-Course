class SimpleCalculator:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

class FunctionalCalculator(SimpleCalculator):
    #add mroe functionality compared to the simple calculator
    def __init__(self):
        super().__init__()


    def inch_to_cm(self, value1):
        return value1 * 2.54

    def triangle_area(self, height, width):
        return height*width/2

    def divisible(self, value1, value2):
        if value2 == 0:
            return False
        elif value1 % value2 == 0:
            return True
        else:
            return False

    def percentage(self, value1, value2):
        if value1 >= 0:
            return value1*100/value2

    def modulus(self, value1, value2):
        return value1 % value2

