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
            self.assertEqual(output, "2004 is a leap year") # Compare output against fizzbuzz.txt
    
    # Use a number not divisible by 4
    def test2(self):
        with captured_output() as (out, err):
            leapyear.ly(2003) # Call leapyear
            output = out.getvalue().strip() # Retrieve ly's output
            self.assertEqual(output, "2003 is not a leap year") # Compare output against fizzbuzz.txt

# call the tests
if __name__ == "__main__":
    unittest.main(verbosity=2)