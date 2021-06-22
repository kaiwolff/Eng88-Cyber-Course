from functional_calculator import FunctionalCalculator

class PromptingCalculator(FunctionalCalculator):

    def __init__(self):
        super().__init__()
        self.available_operations = ["add", "subtract", "multiply", "divide", "divisible", "inch_to_cm", "Triangle_Area"]

    def take_input(self):
        # take input on what operation they want performed
        while True:
            op_type = input(
                f"Please select your operation. Choose from {self.available_operations}. Type 'exit' to exit: ")

            if "exit" in op_type.lower():
                break
            elif op_type in self.available_operations:
                self.run_operation(op_type)

            else:
                print("Input not recognised, please try again.")
                continue

    def run_operation(self,op_type):

        if op_type == "add":
            val_1 = int(input("please input your first value: "))
            val_2 = int(input("please input your second value "))
            print(self.add(val_1, val_2))

        elif op_type == "subtract":
            val_1 = int(input("please input your first value: "))
            val_2 = int(input("please input your second value "))
            print(self.subtract(val_1, val_2))

        elif op_type == "multiply":
            val_1 = int(input("please input your first value: "))
            val_2 = int(input("please input your second value "))
            print(self.multiply(val_1, val_2))

        elif op_type == "divide":
            val_1 = int(input("please input your first value: "))
            val_2 = int(input("please input your second value "))
            print(self.divide(val_1, val_2))

        elif op_type == "divisible":
            val_1 = int(input("please input your first value: "))
            val_2 = int(input("please input your second value "))
            print(self.divisible(val_1, val_2))

        elif op_type == "inch_to_cm":
            val_1 = int(input("please input your value: "))
            print(self.inchtocm(val_1))

        elif op_type == "Triangle_Area":
            val_1 = int(input("please input your Triangle height: "))
            val_2 = int(input("please input your Triangle width:  "))
            print(self.divisible(val_1, val_2))

my_calc = PromptingCalculator()
my_calc.take_input()