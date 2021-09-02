#!/usr/bin/env python3

from typing import NewType

User = NewType(name="User", tp=dict)
underlying_dict = {"name": "Craig Venter"}
some_user = User(underlying_dict)
print(some_user)


def get_name(user: User):
    return user["name"]


print(get_name({"name": "somedict"}))

print(get_name(some_user))

print(some_user == underlying_dict)  # True
print(some_user is underlying_dict)  # True


