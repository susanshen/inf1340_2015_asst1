#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Code written by Deanna Wong and Shu Yun (Susan) Shen

#Determine if Lakshmi made a profit or loss from sale of stocks

#Initial purchase made by Lakshimi
shares = 2000
cost_per_share = 900.00
commission_rate = 0.03

stock_purchased = shares * cost_per_share
commission = commission_rate * stock_purchased
amount_paid = stock_purchased + commission

#Calculation after sale of stocks
cost_per_share = 942.75
stock_sold = shares * cost_per_share
amount_remaining = stock_sold - amount_paid
print "Amount Lakshmi had left after selling stock:", "$", amount_remaining

#Calculation after commission is payed off to determine amount remaining
commission = commission_rate * stock_sold
total_amount_left = amount_remaining - commission
print "Amount Lakshmi had left after paying for commission:", "$", total_amount_left

#Print if Lakshmi made a profit or loss
if total_amount_left < 0:
    print "Lakshmi lost money"
else:
    print "Lakshmi made a profit"


