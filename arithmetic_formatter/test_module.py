#!/usr/bin/python3
from arithmetic_arranger import *
import pytest


def test_display_the_answer():
    actual = arithmetic_arranger(["22 - 5", "32 + 8", "1 + 345", "9999 + 9999"], True)
    assert actual is not None

def test_not_display_the_answer():
    actual = arithmetic_arranger(["22 - 5", "32 + 8", "1 + 345", "9999 + 9999"], False)
    assert actual is None

def test_too_many_problems():
    actual = arithmetic_arranger(["22 - 5", "32 + 8", "1 + 3801", "9999 + 9999", "523 - 49", "32 + 21"], True)
    expected = "Error: Too many problems"
    assert actual == expected

def test_operator_must_be__():
    actual = arithmetic_arranger(["22 - 5", "32 + 8", "1 + 3801", "9999 * 9999"], True)
    expected = "Error: Operator must be '+' or '-'"
    assert actual == expected

def test_numbers_must_contain_digits():
    actual = arithmetic_arranger(["22 - 5", "32 + 8", "1 + Hello", "9999 + 9999"], True)
    expected = "Error: Numbers must only contain digits."
    assert actual == expected

def test_numbers_cannot_be_more_than_4_digits():
    actual = arithmetic_arranger(["22 - 5", "32 + 8", "1 + 12345", "9999 + 9999"], True)
    expected = "Error: Numbers cannot be more than four digits."
    assert actual == expected

if __name__=='__main__':
    pytest.main(['test_module.py','--verbose'])
