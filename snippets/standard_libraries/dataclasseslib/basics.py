#!/usr/bin/env python3
import dataclasses


@dataclasses.dataclass(order=True)
class LabMeasurement:
    name: str
    value: int  # int to keep it basic
    unit: str

    def display(self):
        print(f"{self.name}: {self.value} {self.unit}")


class TestLabMeasurement:
    def test__init__(self):
        name = "testosterone"
        value = 35
        unit = "nmol/l"
        measurement = LabMeasurement(name, value, unit)

        assert measurement.name == name
        assert measurement.value == value
        assert measurement.unit == unit

    def test_set(self):
        name = "testosterone"
        value = 35
        unit = "nmol/l"
        measurement = LabMeasurement(name=name, value=value, unit=unit)

        new_value = 36
        measurement.value = new_value

        assert measurement.name == name
        assert measurement.value == new_value
        assert measurement.unit == unit

    def test_eq(self):
        name = "testosterone"
        value = 35
        unit = "nmol/l"
        measurement = LabMeasurement(name=name, value=value, unit=unit)
        measurement2 = LabMeasurement(name="estrogen", value=value, unit=unit)

        assert measurement == measurement
        assert measurement2 == measurement2
        assert measurement != measurement2

    def test_cmp(self):
        name = "testosterone"
        value = 35
        unit = "nmol/l"
        measurement = LabMeasurement(name=name, value=value, unit=unit)
        measurement2 = LabMeasurement(name="estrogen", value=value, unit=unit)

        assert measurement > measurement2
        assert measurement >= measurement2
        assert (measurement <= measurement2) is False
        assert (measurement < measurement2) is False
        assert sorted([measurement, measurement2]) == sorted([measurement2, measurement])

