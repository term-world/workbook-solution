#!/usr/bin/python

def load_registrants(filename: str = ""):
    runners = None
    with open(filename, "r") as fh:
        runners = fh.readlines()
    return runners

print(load_registrants("data/registrants.csv"))
