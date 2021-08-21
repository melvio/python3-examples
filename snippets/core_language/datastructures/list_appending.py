#!/usr/bin/env python3
numbers = [42, 9001]
letters = "ace"

try:
    print(numbers + letters)
except TypeError as err:
    print(err)  # can only concatenate list (not "str") to list

words = ["ace", "in", "hole"]

print(numbers + words)  # [42, 9001, 'ace', 'in', 'hole']
