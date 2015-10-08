#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """


diagnose_car()

# Code written by Deanna Wong and Shu Yun (Susan) Shen

#Input: A question to request user's input with y or n entry, any other entry will result in an error.
#Expected Output: Display proceeding diagnosis until final solution is provided
diagnose_car = raw_input('Is the car silent when you turn the key? (y/n):')

if diagnose_car == "y":
    diagnose_car = raw_input('Are the battery terminals corroded? (y/n):')

    if diagnose_car == "y":
        print('Clean terminals and start again.')
    elif diagnose_car == "n":
        print('Replace cables and try again.')

elif diagnose_car == "n":
    diagnose_car = raw_input('Does the car make a clicking noise? (y/n):')

    if diagnose_car == "y":
        print('Replace the battery')
    elif diagnose_car == "n":
        diagnose_car = raw_input('Does the car crank up but fail to start? (yes/no):')

    if diagnose_car == "y":
        print('Check spark plug connections.')

    elif diagnose_car == "n":
        diagnose_car = raw_input('Does the engine start and then die? (y/n):')

        if diagnose_car == "y":
            diagnose_car = raw_input('Does your car have fuel injection? (y/n):')

            if diagnose_car == "y":
                print('Check to ensure the choke is opening and closing.')
            elif diagnose_car == "n":
                print('Get it in for service.')

        elif diagnose_car == "n":
            print('Engine is not getting enough fuel. Clean fuel pump.')

else:
    print('Error: This answer is invalid. Only answer y or n.')