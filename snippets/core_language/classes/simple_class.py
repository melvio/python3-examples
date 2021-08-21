#!/usr/bin/env python3


class Doctor:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(dr. {self.name})"


print(Doctor(name="Eric Topol"))  # Doctor(dr. Eric Topol)
