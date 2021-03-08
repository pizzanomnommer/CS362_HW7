# Name: Max Radke   Date: March 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 7
# Description: Takes an input and tells if it is a leap year

import math

global Number # Input number variable (str)
global x # Input number variable (int)

def ly(x):
    Number = str(x)

    if x % 4 == 0: # Calculate if leap year
        print(Number + " is a leap year")
    else:
        print(Number + " is not a leap year")