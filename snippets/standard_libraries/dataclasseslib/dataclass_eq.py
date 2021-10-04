#!/usr/bin/env python3
import dataclasses


@dataclasses.dataclass
class LabMeasurement:
    name: str
    value: int  # int to keep it basic
    unit: str


class TestLabMeasurement:
    def test__eq__(self):
        lm = LabMeasurement("Erythrocytes", 6, unit="10^12/L")

        assert lm == LabMeasurement("Erythrocytes", 6, unit="10^12/L")
        assert lm != LabMeasurement("Erythrocytes", 7, unit="10^12/L")


@dataclasses.dataclass
class LabMeasurement2:
    def __init__(self, name, value, unit):
        if len(name) == 0 or len(unit) == 0:
            raise ValueError(f"{name=} or {unit=} is not valid")
        self.name = name
        self.value = value
        self.unit = unit


class TestLabMeasurement2:
    def test__eq__(self):
        lm2 = LabMeasurement2("Erythrocytes", 6, unit="10^12/L")

        assert lm2 == LabMeasurement2("Erythrocytes", 6, unit="10^12/L")

        # warning. This will succeed:
        assert lm2 == LabMeasurement2("Erythrocytes", 7, unit="10^12/L")

        # This will fail. By implementing fields inside __init__, the fields are
        # no longer used automatically in __eq__.
        assert lm2 != LabMeasurement2("Erythrocytes", 7, unit="10^12/L")


lab1 = LabMeasurement("Erythrocytes", 6, unit="10^12/L")
lab2 = LabMeasurement2("Erythrocytes", 6, unit="10^12/L")

print(lab1)  # LabMeasurement(name='Erythrocytes', value=6, unit='10^12/L')

# __repr__ does not get the fields either
print(lab2)  # LabMeasurement2()
