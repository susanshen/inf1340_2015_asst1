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

#Input:
#Requesting users to input the number of sides in order to retrieve the corresponding shape name
name_that_shape = int(raw_input('Enter the number of sides of a regular polygon and we will name that shape:'))


#Input: Triangle has 3 sides
if name_that_shape == 3:
    print('Triangle')
#Input: Square has 4 sides
elif name_that_shape == 4:
    print('Square')
#Input: Pentagon has 5 sides
elif name_that_shape == 5:
    print('Pentagon')
#Input: Hexagon has 6 sides
elif name_that_shape == 6:
    print('Hexagon')
#Input: Heptagon has 7 sides
elif name_that_shape == 7:
    print('Heptagon')
#Input: Octagon has 8 sides
elif name_that_shape == 8:
    print('Octagon')
#Input: Nonagon has 9 sides
elif name_that_shape == 9:
    print('Nonagon')
#Input: Decagon has 10 sides
elif name_that_shape == 10:
    print('Decagon')
#Input: Cannot name shapes that have more than 10 sides
elif name_that_shape > 10:
    print('Error')
#Input: Shapes with less than 3 sides are not a regular polygon
elif name_that_shape < 3:
    print('Error')
