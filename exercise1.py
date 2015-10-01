#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

shares = 2000
stock_purchased = shares * 900.00
fee = 0.03
#Amount Lakshmi paid for stock
commission = fee * stock_purchased
#Amount Lakshmi paid for commission
amount_paid = stock_purchased + commission
#Total amount Lakshmi spent
print "amount paid:","$",amount_paid



stock_sold = shares * 942.75
#Amount Lakshmi earned after selling the stocks
commission = fee * stock_sold
#Amount Lakshmi paid for commission for selling the stocks
amount_sold = stock_sold - commission - amount_paid
#Amount remaining from profit after paying commission
print "amount sold", "$", amount_sold

if amount_sold < 0:
    print "Lakshmi lost money"

