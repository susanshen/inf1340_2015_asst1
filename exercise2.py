#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape(user_input):
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """
#Code written by Deanna Wong and Shu Yun (Susan) Shen

#Requesting users to input the number of sides in order to retrieve the corresponding shape name
#Input: A phrase to request user's input and a text box for users to input a number
#Error: Input limited to numbers between 3-10, any other numbers will result in an error.

#Test Cases:
#Input: 3
#Expected Output: Triangle

#Input: 4
#Expected Output: Square

#Input: 5
#Expected Output: Pentagon

#Input: 6
#Expected Output: Hexagon

#Input: 7
#Expected Output: Heptagon

#Input: 8
#Expected Output: Octagon

#Input: 9
#Expected Output: Nonagon

#Input: 10
#Expected Output: Decagon

#Input: <3
#Expected Output: Error: This is not a regular polygon

#Input:>10
#Expected Output: Error: This is not a regular polygon

user_input = int(raw_input('Enter the number of sides of a regular polygon and we will name that shape:'))

if user_input == 3:
    print('Triangle')
elif user_input == 4:
    print('Square')
elif user_input == 5:
    print('Pentagon')
elif user_input == 6:
    print('Hexagon')
elif user_input == 7:
    print('Heptagon')
elif user_input == 8:
    print('Octagon')
elif user_input == 9:
    print('Nonagon')
elif user_input == 10:
    print('Decagon')
elif user_input > 10:
    print('Error: This program can only name shapes that have up to 10 sides')
elif user_input < 3:
    print('Error: This is not a regular polygon')

name_that_shape(user_input)