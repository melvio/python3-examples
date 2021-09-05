#!/usr/bin/env python3
import pytest


# inspired by: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

def capitize(s: str):
    return s.capitalize()


def test_capitize():
    assert capitize("melvio") == "Melvio"


def test_capitze_raise_on_int():
    with pytest.raises(AttributeError):
        capitize(9)
