# Name: Max Radke   Date: March 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 7
# Description: Tests file "fizzbuzz.py"
#
# How to run: Open the directory that this file is in with command prompt.
#             Make sure that listAvg.py is in the same directory.
#             Type "python ./test_fizzbuzz.py"

import sys
import unittest
import fizzbuzz
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
    # Test stdout against the fizzbuzz.txt file
    def test1(self):
        self.maxDiff = None # Had to make test output max size unbounded (Also removed comma from fizzbuzz.txt)
        CompFile = open("fizzbuzz.txt", "r") # Open fizzbuzz.txt
        with captured_output() as (out, err):
            fizzbuzz.fb() # Call fizzbuzz
            output = out.getvalue().strip() # Retrieve fb's output
            self.assertEqual(output, CompFile.read()) # Compare output against fizzbuzz.txt

# call the tests
if __name__ == "__main__":
    unittest.main(verbosity=2)