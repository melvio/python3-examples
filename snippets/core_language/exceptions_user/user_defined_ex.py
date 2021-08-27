#!/usr/bin/env python3


# <https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions.l
class SmallFailure(Exception):
    def __init__(self, message=None):
        self.message = "no message" if message is None else message

    def __str__(self) -> str:
        return f"SmallFailure: {self.message}"


try:
    raise SmallFailure()
except SmallFailure as e:
    print(e)  # SmallFailure: no message


try:
    raise SmallFailure("failed something small")
except SmallFailure as e:
    print(e)  # SmallFailure: failed something small
