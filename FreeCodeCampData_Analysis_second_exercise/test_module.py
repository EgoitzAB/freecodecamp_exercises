#!/usr/bin/python3
import pytest
from demographic_data_analyzer import demographic_analyzer

def test_race_counting():
    actual = demographic_analyzer(print_responses=False)['race_count'].replace('\n', '')
    expected = '27816 3124 1039  311  271'
    assert actual == expected

def test_average_age_men():
    actual = demographic_analyzer(print_responses=False)['average_age_men']
    expected = 39.4
    assert actual == expected

def test_percentage_bachelors():
    actual = demographic_analyzer(print_responses=False)['bachelors_degree_per']
    expected = 16.4
    assert actual == expected

def test_percentage_earnings_high_edu():
    actual = demographic_analyzer(print_responses=False)['percentage_high_earning_high_edu']
    expected = 46.5
    assert actual == expected

def test_percentage_earnings_low_edu():
    actual = demographic_analyzer(print_responses=False)['percentage_high_earning_low_edu']
    expected = 17.4
    assert actual == expected

def test_minimun_hours_week():
    actual = demographic_analyzer(print_responses=False)['min_work_hours_week']
    expected = 1
    assert actual == expected

def test_rich_percentage():
    actual = demographic_analyzer(print_responses=False)['rich_percentage']
    expected = 10
    assert actual == expected

def test_highest_earning_country():
    actual = demographic_analyzer(print_responses=False)['highest_earning_country']
    expected = 10
    assert actual == expected

def test_highest_earning_country_percentage():
    actual = demographic_analyzer(print_responses=False)['highest_earning_country_percentage']
    expected = 'United-States    91.5'
    assert actual == expected

def test_high_salary_occupation_india():
    actual = demographic_analyzer(print_responses=False)['high_salary_occupation_India']
    expected = 'Prof-specialty'
    assert actual == expected

if __name__=='__main__':
    pytest.main(['test.module.py', '--verbose'])
