#!/usr/bin/python

# Necessary imports
import random
import string

def get_letter():
    """ Generates a single character from a-z;A-Z set """
    letter = random.choice(string.ascii_letters)
    return letter

def get_number():
    """ Generates a 0-9 digit """
    number = random.choice(string.digits)
    return number

def get_symbol():
    """ Generates a symbol character """
    symbol = random.choice(string.punctuation)
    return symbol

# Print introduction
print("Complex password generator", end = "\n\n")
# Ask user for requirement
pass_length = int(input("Enter length of password: "))
# Print menu options
print("""Choose components of password:

    1. Letters
    2. Numbers
    3. Symbols
""")

requirements = ""

# Loop to allow for multiple selections
while True:
    choice = input("Enter number of component to add: ")
    if choice not in requirements:
        requirements += choice
    # If choice is left blank, end selection
    if not choice:
        break

# Generate empty password string
password = ""

# Loop to add individual entries to password
while len(password) < pass_length:
    selection = random.choice(requirements)
    # If letters are a requirement, add a letter
    if selection == "1":
        password += get_letter()
    # If numbers are a requirement, add a number
    if selection == "2":
        password += get_number()
    # If symbols are a requirement, add a symbol
    if selection == "3":
        password += get_symbol()

# Print the generated password
print(f"Password generated: {password}")
