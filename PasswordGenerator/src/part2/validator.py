#!/usr/bin/python

import string

def contains_allowed(generated: str = "", exceptions: str = "") -> bool:
    for char in generated:
        if not exceptions: break
        if char in exceptions:
            print("Contains disallowed character(s)")
            return False
    return True

def contains_upper(generated: str = "") -> bool:
    for char in generated:
        if char.isupper():
            return True
    print("Missing uppercase character")
    return False

def contains_number(generated: str = "") -> bool:
    for char in generated:
        if char.isdigit():
            return True
    print("Missing digit character")
    return False

def validate(generated: str = "", exceptions: str = "") -> bool:
    is_valid = contains_allowed(generated, exceptions)
    is_valid = is_valid and contains_upper(generated)
    is_valid = contains_number(generated)
    return is_valid
