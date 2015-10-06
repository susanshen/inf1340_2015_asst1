#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

#Input: 2000 shares
shares = 2000

#Input: $900 per share
cost_per_share = 900.00

#Calculate amount paid on stocks as 2000 shares multiplied by $900
#Expected output: $1,800,000
stock_purchased = shares * cost_per_share

#Input: 3%
three_percent = 0.03

#Calculate stockbroker's commission as 0.03 multiplied by $1,800,000
#Expected Output: $54,000
commission = three_percent * stock_purchased

#Calculate the total amount Lakshmi spent as $1,800,000 multiplied by $54,000
#Expected output: $1,854,000
amount_paid = stock_purchased + commission


#Input: $942.75 per share two weeks later
cost_per_share = 942.75

#Calculate amount of money made after selling stock as 2000 shares multiplied by $942.75
#Expected Output: $1,885,500
stock_sold = shares * cost_per_share

#Calculate Lakshmi's profit after selling stock as $1,854,000 subtracted from $1,885,500
#Expected Output: $31,5000
amount_left_selling_stock = stock_sold - amount_paid

#Display Lakshmi's profit after selling stock
print "Amount Lakshmi had left after selling stock:", "$", amount_left_selling_stock


#Calculate stockbroker's commission as 0.03 multiplied by $1,885,500
#Expected Output: $56,565
commission = three_percent * stock_sold

#Calculate amount remaining after paying for commission as $56,565 subtracted from $31,5000
#Expected Output: $-25,065
total_amount_left = amount_left_selling_stock - commission

#Display Amount Lakshmi had left after paying for commission
print "Amount Lakshmi had left after paying for commission:", "$", total_amount_left

#Lakshmi lost money if the amount of money left is negative
if total_amount_left < 0:
    print "Lakshmi lost money"
#Lakshmi made a profit if amount of money left is positive (anything other than negative)
else:
    print "Lakshmi made a profit"


