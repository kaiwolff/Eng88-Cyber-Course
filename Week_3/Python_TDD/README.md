## Test-Driven Development

Test-Driven Development is an approach where tests are written first, and then the simplest code to pass the tests is written, in order to quickly produce a prgram conforming to a set of customer requirements. The code is then refactored and more tests are written if necessary, starting the cycle again.


### TDD Exercise

Trying out a TDD approach to writing a calculator

First, we ensure that pytest is installed as we need this to run our tests.

Since we are trialling Test-Driven Development, we write the tests before the code, defining what functions we want to have in our calculator and what we want them to return for our test cases.

To do this, we create a class that inherits from the TestCase class in the unittest library. This class lets us run methods to test the functionality of our code. We also need to have imported the classes we want to test.

After that we simply define what we require the test case to return when we run a function with a set of inputs. Instantiating an object of the testable code in our test case and then defining the functions lets us run the test case to make sure the code does what we want it to. The full code is below:

```python
#this file requires pytest to be installed.
import pytest
import unittest

from functional_calc import FunctionalCalculator

class FunctionalCalcTest(unittest.TestCase):

class FunctionalCalcTest(unittest.TestCase):

    calc = FunctionalCalculator()

    def test_add(self): # naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter recognises it as a testcase.
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 4), 0.5)

    def test_inch_to_cm(self):
        self.assertEqual(self.calc.inch_to_cm(2), 5.08)

    def test_triangle_area(self):
        self.assertEqual(self.calc.triangle_area(2,2),2.0)

    def test_divisible(self):
        self.assertEqual(self.calc.divisible(2,0), False)
        self.assertEqual(self.calc.divisible(2,3), False)
        self.assertEqual(self.calc.divisible(2,2), True)
        
    
    def test_percentage(self):
        self.assertEqual(self.calc.percentage(1,2), 50.0)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(self,1,2), 1)


```

Notice that all testing functions start with `test`, which is important as it is needed for the interpreter to recognise them as tests. Also notice that the test of divisible has three test cases, one for each branch of the intended control flow.

Now that we have defined what tests we want our code to pass, we write code to pass these tests. As this exercise is about the TDD approach, I took my calculator code from a previous iteration. I did this through two classes:

```python
#file named oop_calculator
class SimpleCalculator:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

```
We have to have the parent class, SimpleCalculator available.

```python

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
```
This code fails two of the tests, as the functions modulus and percentage are not yet available. Therefore, we have to write code to pass our tests, meaning we need to add the below to `FunctionalCalculator`:
```python

    def percentage(self, value1, value2):
        if value1 >= 0:
            return value1*100/value2

    def modulus(self, value1, value2):
        return value1 % value2

```

Simple Calculator could also be tested separately, meaning that we would only need to test the additional functions in functional_calc.

## Notes:

- Test cases have to start the function name with `test` in order to be recognised by the interpreter. 
- Ideally, tests should cover any ways a user might conceivably input something that causes problems with the code.