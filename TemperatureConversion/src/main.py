#!/usr/bin/python

"""
Temperature converstion program used to demonstrate:

* interactive programs
* data types
* basic computation

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

# Print program name
print("Farenheight to celsius converter", end = "\n\n")
# Request user input
temp_in_f = input("Enter the temperature (without units): ")
# Perform calculation
temp_in_c = int(temp_in_f) - 32
temp_in_c *= 5 / 9
# Report result
print(f"The temperature ({temp_in_f}F) is: {temp_in_c:.{1}f}C")
