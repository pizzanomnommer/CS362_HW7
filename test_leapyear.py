# Name: Max Radke   Date: March 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 7
# Description: Tests file "leapyear.py"
#
# How to run: Open the directory that this file is in with command prompt.
#             Make sure that leapyear.py is in the same directory.
#             Type "python ./test_leapyear.py"

import sys
import unittest
import leapyear
from contextlib import contextmanager
import io

# Used to read stdout and stderr
@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestListAvg(unittest.TestCase):
    # Test a leap year that is only divisible by 4
    def test1(self):
        with captured_output() as (out, err):
            leapyear.ly(2004) # Call leapyear
            output = out.getvalue().strip() # Retrieve ly's output
            self.assertEqual(output, "2004 is a leap year")
    
    # Use a number not divisible by 4
    def test2(self):
        with captured_output() as (out, err):
            leapyear.ly(2003) # Call leapyear
            output = out.getvalue().strip() # Retrieve ly's output
            self.assertEqual(output, "2003 is not a leap year")

    # Use a number both divisible by 4 and 100, but not 400
    def test3(self):
        with captured_output() as (out, err):
            leapyear.ly(2100) # Call leapyear
            output = out.getvalue().strip() # Retrieve ly's output
            self.assertEqual(output, "2100 is not a leap year")

    # Use a number both divisible by 4 and 100, and also by 400
    def test4(self):
        with captured_output() as (out, err):
            leapyear.ly(2000) # Call leapyear
            output = out.getvalue().strip() # Retrieve ly's output
            self.assertEqual(output, "2000 is a leap year")

    # Integers only
    def test5(self):
        with self.assertRaises(TypeError):
            leapyear.ly("2000")

    # No negatives
    def test6(self):
        with self.assertRaises(ValueError):
            leapyear.ly(-2000)

# call the tests
if __name__ == "__main__":
    unittest.main(verbosity=2)