# The FizzBuzz task

My first iteration was to simply ensure the logic was being executed correctly

```
for i in range(1,101):
    #set up conditions. Priorities are:
    # 1. Fizzbuzz, as we want to print neither fizz nor buzz, but a combo
    # 2. is it it fizz or buzz, as we don't want to print hte number if it fizzes or buzzes
    # 3. print the number if no conditions met
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:#no fizzbuzz, check for fizz
        print("Fizz")
    elif i % 5 == 0: #No fizzbuzz, no fizz, check for buzz
        print("Buzz")
    else: #if nothign else print the number
        print(i)

```
Note that placing Fizzbuzz as the first if statement ensures no duplicate printouts for FizzBuzz numbers. I initially only used printouts, and haven't yet packaged the logic into a class and method format.

### Second Iteration

I have now packaged the logic in a method called ```fizz_buzz_checker```. Given a desired range, it will give everythign from 1 to that number, up to and including the value given:

```# The Problem
#
# "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
#
# NOTE -> Must be in class and method format

class FizzBuzz():

    #made it a static method initially as this means I can call the method without instantiating
    def fizz_buzz_checker(self, max_val):
        #Takes in a maximum value, and will print everything from one up to an including that value. If Fizz, Buzz or Fizzbuzz criteria are fullfilled, returns that statement
        for i in range((max_val + 1)):
            if i % 3 == 0 and i % 5 == 0: #Check for FizzBuzz
                print("FizzBuzz")
            elif i % 3 == 0:#no fizzbuzz, check for fizz
                print("Fizz")
            elif i % 5 == 0: #No fizzbuzz, no fizz, check for buzz
                print("Buzz")
            else: #if nothing else return the number
                print(i)
                
```

Test case passes as planned:

```
# test for max_val = 100
my_fizzbuzz = FizzBuzz()
my_fizzbuzz.fizz_buzz_checker(100)
```

Next Step might be to allow a variety of Fizz or Buzz criteria, adjust step size, etc.