#!/usr/bin/env python3

import pytest


class MedicalITSpecialist:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class TestMedicalSpecialty:
    @pytest.fixture
    def some_specialty(self) -> MedicalITSpecialist:
        return MedicalITSpecialist("EHR implementation specialist")

    # 'some_specialty' is injected by @pytest.fixture
    # Pytest will inject an argument if the annotated function name
    #  matches the parameter name.
    @pytest.fixture
    def some_specialty_list(self,
                            some_specialty: MedicalITSpecialist) -> [MedicalITSpecialist]:
        return [some_specialty, MedicalITSpecialist("Medical Software Developer")]

    def test_my_it_specialist(self, some_specialty, some_specialty_list):
        assert some_specialty in some_specialty_list
