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

    Inputs: 3-10

    Expected Outputs: Corresponding shapes

    Errors: Input limited to numbers between 3-10, any other numbers will result in an error.

    """
    #Test Cases:
    #Input: 3
    #Expected Output: triangle
    #Input: 4
    #Expected Output: quadrilateral
    #Input: 5
    #Expected Output: pentagon
    #Input: 6
    #Expected Output: hexagon
    #Input: 7
    #Expected Output: heptagon
    #Input: 8
    #Expected Output: octagon
    #Input: 9
    #Expected Output: nonagon
    #Input: 10
    #Expected Output: decagon
    #Input: <3
    #Expected Output: Error
    #Input: >10
    #Expected Output: Error

    user_input = raw_input('Enter the number of sides of a regular polygon and we will name that shape:')

    if user_input == "3":
        print('triangle')
    elif user_input == "4":
        print('quadrilateral')
    elif user_input == "5":
        print('pentagon')
    elif user_input == "6":
        print('hexagon')
    elif user_input == "7":
        print('heptagon')
    elif user_input == "8":
        print('octagon')
    elif user_input == "9":
        print('nonagon')
    elif user_input == "10":
        print('decagon')
    elif user_input > "10":
        print('Error')
    elif user_input < "3":
        print('Error')

#name_that_shape()