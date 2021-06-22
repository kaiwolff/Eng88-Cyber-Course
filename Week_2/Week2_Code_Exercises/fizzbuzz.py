# The Problem
#
# "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
#
# NOTE -> Must be in class and method format

class FizzBuzz():

    #made it a static method initially as this means I can call the method without instantiating
    def fizz_buzz_checker(self, max_val):
        #Takes in a maximum value, and will print everything from one up to an including that value. If Fizz, Buzz or Fizzbuzz criteria are fullfilled, returns that statement
        for i in range(1,max_val + 1):
            if i % 3 == 0 and i % 5 == 0: #Check for FizzBuzz
                print("FizzBuzz")
            elif i % 3 == 0:#no fizzbuzz, check for fizz
                print("Fizz")
            elif i % 5 == 0: #No fizzbuzz, no fizz, check for buzz
                print("Buzz")
            else: #if nothing else return the number
                print(i)

# test for max_val = 100
my_fizzbuzz = FizzBuzz()
my_fizzbuzz.fizz_buzz_checker(100)