#!/usr/bin/python

"""
Basic power/root calcuation program to demonstrate:

* functions
* arguments
  * defaults
* parameters

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

# Necessary imports
import math
import suffix

def raise_to_power(number: int = 0, power: float = 1.0):
    """ Calculates result of various numbers raised to various powers. """
    sqr_root = math.pow(number, power)
    return sqr_root

def calc_root(number: int = 0, root: float = 1.0):
    """ Calculates nth root of a number by raising to fractional power """
    nth_root = raise_to_power(number, 1 / root)
    return nth_root

# Print program introduction
print("Power and root calculator", end = "\n\n")

# Collect user information
user_num = int(input("Enter a number: "))
user_pow = int(input("Enter a power: "))

# Perform calculations using functions
raised = raise_to_power(user_num, user_pow)
rooted = calc_root(user_num, user_pow)

# The the proper number suffix: 1st, 2nd...
num_suffix = suffix.determine(user_pow)

# Print results for both computations using same power
print(f"{user_num} raised to the {user_pow}{num_suffix} power: {raised}")
print(f"{user_num} taken to the {user_pow}{num_suffix} root: {rooted}")
