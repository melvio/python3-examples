#!/usr/bin/env python3
import pytest


def api_logic_to_percentage(api_points: int):
    """We get a value of an API.
    At 0 were at 0%, at 1 were at 2%, at 2 were at 4%, etcetera.
    As magic value, this API returns -1 when we are done.
    Values are always between 0 and 49 (inclusive)
    """
    if api_points == -1:
        return 100
    return api_points * 2


@pytest.mark.parametrize(
    "api_points,expected_percentage",
    [(-1, 100), (2, 4), (5, 10), (14, 28), (37, 74)]
)
def test_api_logic_to_percentage(api_points, expected_percentage):
    assert api_logic_to_percentage(api_points) == expected_percentage


def fair_to_explain(char: str):
    mapping = {"F": "Findable",
               "A": "Accessible",
               "I": "Interoperable",
               "R": "Reusable"}
    return mapping.get(char)


@pytest.mark.parametrize(
    "char,explanation",
    [("F", "Findable"), ("A", "Accessible"), ("I", "Interoperable"), ("R", "Reusable")]
)
def test_fair_to_explain_ok(char, explanation):
    assert fair_to_explain(char) == explanation


def test_fair_to_explain_fail():
    assert fair_to_explain("O") is None
