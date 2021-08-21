#!/usr/bin/env python3
l = ["a", "bc", "def"]

print(l[0])  # "a"

try:
    print(l[3])
except IndexError as err:
    print(err)  # list index out of range
