class Calculator:
    #made them static methods so that I don't have to create an object.
    def add(self, value1, value2) : return value1 + value2

    def subtract(self, value1, value2): return value1 - value2

    def multiply(self, value1, value2) : return value1 * value2

    def divide(self, value1, value2) : return value1 / value2

    def divisible(self, value1, value2):
        if value2 == 0:
            return False
        elif value1 % value2 == 0:
            return True
        else:
            return False

    def inchtocm(self, value1): return value1 * 2.54

    def triangle_area(self, height, width): return height*width/2



#Test Cases
# my_calc = Calculator()
