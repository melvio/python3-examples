#!/usr/bin/env python3


class Doctor:
    def __init__(self, specialty):
        self.specialty = specialty

    def __str__(self):
        return self.__class__.__name__ + "(" + f"specialty={self.specialty}" + ")"


class Internist(Doctor):

    def __init__(self):
        super().__init__("internist")


if __name__ == "__main__":
    print(Internist())  # Internist(specialty=internist)
