# get user input of a float number
# check if the number is lower than .50 then round the figure to lower end
# check if the number is greater than .51 then round the figure to higher end
# example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end

import math
from input_control import input_float

num_float = input_float()

if "exit" in num_float:
    exit

#subtracting the rounded down number leaves only the decimal part.
# then applying control flow. Could also have been solved by using int(num_float), which works quite similarly to math.floor.
else:
    if num_float - math.floor(num_float) > 0.50:
        print(math.ceil(num_float))
    else:
        print(math.floor(num_float))
