def input_float(): #makes sure that the input is a float
    #Will either return the input as a float or the phrase "exit"
    while True:
        var = input(f"Please enter a float. Type 'exit' to exit: ")
        if "exit" in var.lower():
            return "exit"
        else:
            try:
                return float(var)
            except:
                print("input not recognised")
                continue


def input_float_range(min_val, max_val): #makes sure that the input is a float within a set range
    #Will either return the input as a float or the phrase "exit"
    while True:
        var = input(f"Please enter a float between {min_val} and {max_val}. Type 'exit' to exit: ")
        if "exit" in var.lower():
            return "exit"
        else:
            try:
                float(var)
            except:
                print("input not recognised")
                continue

        if float(var) <= max_val and float(var) >=min_val:
            return float(var)
        else:
            print(f"Input must be between {min_val} and {max_val}. Please try again")
            continue

def input_int(): #makes sure that the input is a int
    #Will either return the input as an int or the phrase "exit"
    while True:
        var = input(f"Please enter an integer. Type 'exit' to exit: ")
        if "exit" in var.lower():
            return "exit"
        else:
            try:
                return int(var)
            except:
                print("Input not recognised")
                continue

def input_int_range(min_val, max_val): #makes sure that the input is an integer within a set range
    #Will either return the input as an integer or the phrase "exit"
    while True:
        var = input(f"Please enter an integer between {min_val} and {max_val}. Type 'exit' to exit: ")
        if "exit" in var.lower():
            return "exit"
        else:
            try:
                int(var)
            except:
                print("input not recognised")
                continue

        if int(var) <= max_val and int(var) >=min_val:
            return int(var)
        else:
            print(f"Input must be between {min_val} and {max_val}. Please try again")
            continue
def input_yes_no():
    #will return true, false, or exit, depending on the user choice. Continually prompts user until acceptable option reached
    while True:
        var = input("Please input 'y' or 'n' to signify yes or no. Type 'exit to exit: ")
        if "exit" in var.lower():
            return "exit"
        elif var.lower() == "y":
            return True
        elif var.lower() == "n":
            return False
        else:
            print("Input not recognised")
            continue