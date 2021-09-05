#!/usr/bin/env python3


class User:
    def __init__(self, user_info):
        self.user_info = user_info

    def __getitem__(self, key):
        """__getitem__ dunder method implements the D[key] syntax"""
        return self.user_info.__getitem__(key)


user = User(user_info={"name": "melvin", "age": 28})

print(user["name"])  # melvin
