#!/usr/bin/env python3


class Doctor:
    def __init__(self, *, name, age, specialty):
        self.name = name
        self.age = age
        self.specialty = specialty


laennec = Doctor(name="René Laënnec", age=45, specialty=None)

print(getattr(laennec, "age"))  # 45

print(laennec.__dict__)  # {'name': 'René Laënnec', 'age': 45, 'specialty': None}
