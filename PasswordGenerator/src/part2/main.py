#!/usr/bin/python

# Necessary imports
import random
import string

import validator

def get_letter():
    """ Generates a single character from a-z;A-Z set """
    letter = random.choice(string.ascii_letters)
    return letter

def get_number():
    """ Generates a 0-9 digit """
    number = random.choice(string.digits)
    return number

def get_symbol(disallowed: str = ""):
    """ Generates a symbol character """
    is_allowed = False
    while not is_allowed:
        symbol = random.choice(string.punctuation)
        if symbol not in disallowed:
            is_allowed = True
    return symbol

def generate(length: int = 0, requirments: str = "", exceptions: str = ""):
    # Generate empty password string
    password = ""
    # Loop to add individual entries to password
    while len(password) < length and requirements:
        selection = random.choice(requirements)
        # If letters are a requirement, add a letter
        if selection == "1":
            password += get_letter()
        # If numbers are a requirement, add a number
        elif selection == "2":
            password += get_number()
        # If symbols are a requirement, add a symbol
        elif selection == "3":
            password += get_symbol(exceptions)
    return password

def validate(generated: str = "", length: int = 0, exceptions: str = ""):
    """ Validates according to mandated password requirements """
    is_valid = validator.validate(generated, exceptions)
    if is_valid and length == len(generated):
        return True
    return False

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

not_allowed = None
if "3" in requirements:
    not_allowed = input("Enter disallowed characters: ")

password = generate(pass_length, requirements, not_allowed)
is_valid = validate(password, pass_length, not_allowed)

status = "VALID" if is_valid else "INVALID"

# Print the generated password
print(f"Password generated: {password} ({status})")
