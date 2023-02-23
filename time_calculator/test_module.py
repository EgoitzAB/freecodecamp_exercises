#!/usr/bin/python3
from time_calculator import *
import pytest

def test_add_time_same_day_PM():
    actual = add_time("3:00 PM", "4:25")
    expected = "7:25 PM"
    assert actual == expected

def test_add_time_same_day_AM():
    actual = add_time("3:00 AM", "4:25")
    expected = "7:25 AM"
    assert actual == expected

def test_add_time_same_day_AM_PM():
    actual = add_time("3:00 AM", "14:25")
    expected = "5:25 PM"
    assert actual == expected

def test_add_time_00_case():
    actual = add_time("3:45 AM", "11:20")
    expected = "3:05 PM"
    assert actual == expected

def test_add_time_next_day_morning():
    actual = add_time("3:00 PM", "14:25")
    expected = "5:25 AM (next day)"
    assert actual == expected

def test_add_time_next_day_noon():
    actual = add_time("3:00 AM", "26:25")
    expected = "5:25 PM (next day)"
    assert actual == expected

def test_add_time_next_days_noon():
    actual = add_time("3:00 PM", "47:25")
    expected = "2:25 PM (2 days later)"
    assert actual == expected

def test_add_time_next_days_noon_00_case():
    actual = add_time("3:00 PM", "47:05")
    expected = "2:05 PM (2 days later)"
    assert actual == expected

def test_add_time_next_days_noon_AM_PM():
    actual = add_time("3:00 PM", "59:25")
    expected = "2:25 AM (3 days later)"
    assert actual == expected

def test_add_time_next_days_morning():
    actual = add_time("3:00 PM", "35:25")
    expected = "2:25 AM (2 days later)"
    assert actual == expected

def test_add_time_same_day_AM_day():
    actual = add_time("3:00 AM", "4:10", "Wednesday")
    expected = "7:10 AM, Wednesday"
    assert actual == expected

def test_add_time_same_day_PM_day():
    actual = add_time("3:00 PM", "4:10", "Wednesday")
    expected = "7:10 PM, Wednesday"
    assert actual == expected

def test_add_time_same_day_AM_PM_day():
    actual = add_time("3:00 AM", "14:10", "Wednesday")
    expected = "5:10 PM, Wednesday"
    assert actual == expected

def test_add_time_next_day_morning_day():
    actual = add_time("3:00 PM", "14:25", "Saturday")
    expected = "5:25 AM, Sunday (next day)"
    assert actual == expected

def test_add_time_next_day_noon_day():
    actual = add_time("3:00 PM", "24:25", "Saturday")
    expected = "3:25 PM, Sunday (next day)"
    assert actual == expected

def test_add_time_next_days_noon_day():
    actual = add_time("3:00 PM", "47:25", "Monday")
    expected = "2:25 PM, Wednesday (2 days later)"
    assert actual == expected

def test_add_time_next_days_noon_day_upper_lower():
    actual = add_time("11:43 PM", "24:20", "MoNdaY")
    expected = "0:03 AM, Wednesday (2 days later)"
    assert actual == expected

def test_add_time_next_days_noon_day_lower_upper():
    actual = add_time("3:00 PM", "47:25", "moNdaY")
    expected = "2:25 PM, Wednesday (2 days later)"
    assert actual == expected




if __name__=='__main__':
    pytest.main(['test.module.py', '--verbose'])
