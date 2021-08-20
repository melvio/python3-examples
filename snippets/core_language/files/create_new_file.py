#!/usr/bin/env python3

with open("new_file.txt", "w") as new_file:
    new_file.write("hiyaa\nHow ur doin?\n")

print("new_file.closed", new_file.closed)  # new_file.closed True

with open("new_file.txt", "r") as created_file:
    lines = created_file.readlines()
    for line in lines:
        print(line, end='')
        # hiyaa
        # How ur doin?
    print("created_file.closed", created_file.closed)  # created_file.closed False

print("created_file.closed", created_file.closed)  # created_file.closed True
