#!/usr/bin/env python3
import dataclasses


@dataclasses.dataclass()
class LabMeasurement:
    # https://docs.python.org/3/library/dataclasses.html#post-init-processing
    name: str
    value: float
    unit: str = None

    def __post_init__(self):
        print(f"__post_init__ {self.name=}")
        if self.name == "":
            raise ValueError("name cannot be empty")


urine_lab = LabMeasurement(name="albumine", value=110.1, unit="mg/24h")
print(urine_lab)

urine_lab2 = LabMeasurement(name="", value=110.1, unit="mg/24h")
