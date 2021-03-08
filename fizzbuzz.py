# Name: Max Radke   Date: March 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 7
# Description: Prints numbers 1-100, but every multiple
#               of 3 gets replaced with 'fizz' and every
#               multiple of 5 gets replaced with 'buzz'.
#               multiples of both get replaced with 'fizzbuzz'

def fb():
    # Go from 0 - 99
    for x in range(100):
        output = "" # Set empty output
        if (x + 1) % 3 == 0: # Add 1 to x to get from 1 - 100
            output = "Fizz" # Fizzable
        if (x + 1) % 5 == 0:
            output = output + "Buzz" # Buzzable
        if output == "": # Not fizz or buzzable, print number instead
            output = str(x + 1)
        print(output)