#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """

name_that_shape()

# Code written by Deanna Wong and Shu Yun (Susan) Shen

#Requesting users to input the number of sides in order to retrieve the corresponding shape name
#Input: A phrase to request user's input and a text box for users to input a number
#Input limited to numbers between 3-10, any other numbers will result in an error.

name_that_shape = int(raw_input('Enter the number of sides of a regular polygon and we will name that shape:'))

if name_that_shape == 3:
    print('Triangle')

elif name_that_shape == 4:
    print('Square')

elif name_that_shape == 5:
    print('Pentagon')

elif name_that_shape == 6:
    print('Hexagon')

elif name_that_shape == 7:
    print('Heptagon')

elif name_that_shape == 8:
    print('Octagon')

elif name_that_shape == 9:
    print('Nonagon')

elif name_that_shape == 10:
    print('Decagon')

elif name_that_shape > 10:
    print('Error: This program can only name shapes that have up to 10 sides')

elif name_that_shape < 3:
    print('Error: This is not a regular polygon')

