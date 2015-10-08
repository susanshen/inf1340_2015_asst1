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

    Inputs: Y or N

    Expected Outputs: Display proceeding diagnosis until final solution is provided

    Errors: Any other entry besides y and n will result in an error

    Test Case:
    #Input:Y
    #Expected Output: Display Are the battery terminals corroded? (Y/N):
    #Input:YY
    #Expected Output: Display Clean terminals and try starting again.
    #Input:YN
    #Expected Output: Display Replace cables and try again.
    #Input:N
    #Expected Output: Display Does the car make a clicking noise? (Y/N):
    #Input:NY
    #Expected Output: DisplayReplace the battery
    #Input:NN
    #Expected Output: Display Does the car crank up but fail to start? (Y/N):
    #Input:NNY
    #Expected Output: Display Check spark plug connections.
    #Input:NNN
    #Expected Output: Display Does the engine start and then die? (Y/N):
    #Input:NNNY
    #Expected Output: Display Does your car have fuel injection? (Y/N):
    #Input:NNNYN
    #Expected Output: Display Check to ensure the choke is opening and closing.
    #Input:NNNYY
    #Expected Output: Display Get it in for service.
    #Input:NNNN
    #Expected Output: Display Engine is not getting enough fuel. Clean fuel pump.
    #Input: Anything other than Y and N
    #Expected Output: Display Error: This answer is invalid. Only answer Y or N.
    """


    user_input = raw_input('Is the car silent when you turn the key? (Y/N):')

    if user_input == "Y":
        user_input = raw_input('Are the battery terminals corroded? (Y/N):')

        if user_input == "Y":
            print('Clean terminals and try starting again.')

        elif user_input == "N":
            print('Replace cables and try again.')

    elif user_input == "N":
        user_input = raw_input('Does the car make a clicking noise? (Y/N):')

        if user_input == "Y":
            print('Replace the battery.')

        elif user_input == "N":
            user_input = raw_input('Does the car crank up but fail to start? (Y/N):')

            if user_input == "Y":
                print('Check spark plug connections.')

            elif user_input == "N":
                user_input = raw_input('Does the engine start and then die? (Y/N):')

                if user_input == "Y":
                    user_input = raw_input('Does your car have fuel injection? (Y/N):')

                    if user_input == "N":
                        print('Check to ensure the choke is opening and closing.')

                    elif user_input == "Y":
                        print('Get it in for service.')

                elif user_input == "N":
                    print('Engine is not getting enough fuel. Clean fuel pump.')

        else:
            print('Error: This answer is invalid. Only answer Y or N.')

#diagnose_car()