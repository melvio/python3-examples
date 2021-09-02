#!/usr/bin/env python3

from typing import List

Doses = List[float]


# Doses = list[float] # python 3.9


def increase_dose(increase_factor: float, doses: Doses) -> Doses:
    return [increase_factor * dose for dose in doses]


old_doses = [1.7, 22.3, 100.]
new_doses: Doses = increase_dose(increase_factor=1.1, doses=old_doses)
print(new_doses)
