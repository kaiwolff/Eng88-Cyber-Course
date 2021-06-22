#this file requires pytest to be installed.
import pytest
import unittest

from functional_calc import FunctionalCalculator

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
        self.assertEqual(self.calc.modulus(1,2), 1)
